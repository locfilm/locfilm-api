""" Bookings views """
# Django
from django.core import exceptions

# DRF
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as status_codes

# Python
from datetime import datetime

# App data
from locfilm.bookings.serializers import BookingSerializer, DatesBookingSerializer
from locfilm.bookings.serializers import UpdateBookingStatusSerializer
from locfilm.bookings.models import Booking
from locfilm.locations.models import Rating
from locfilm.locations.models import Location
from locfilm.users.models import User
from locfilm.bookings.permissions import OwnProfilePermission
from locfilm.locations.serializers.ratings import RatingModelSerializer


class BookingViewSet(viewsets.ModelViewSet):
    # specify serializer to be used
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(booking__username=username)
        return queryset

    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAuthenticated])
    def update_status(self, request, pk=None):
        try:
            booking = Booking.objects.get(id=pk)
        except exceptions.ObjectDoesNotExist:
            return Response({'error': 'Location with ID provided does not exist'},
                            status=status_codes.HTTP_404_NOT_FOUND)

        if request.user != booking.user_id:
            return Response({'error': 'User unauthorized'}, status=status_codes.HTTP_401_UNAUTHORIZED)

        data = request.data
        serializer = UpdateBookingStatusSerializer(booking, data=data, partial=True)
        if not serializer.is_valid():
            return Response({'error': serializer.errors,
                             'required': 'One value: "Pending","Confirmed", "Cancelled", "Finished"'},
                            status=status_codes.HTTP_400_BAD_REQUEST)

        status = serializer.validated_data['status']
        error = False
        message = ''

        if booking.status == 'Pending':
            if status == 'Confirmed' or status == 'Cancelled':
                serializer.validated_data['status'] = status
            else:
                error = True
                message = f'The status of the booking cannot be changed because its status is {booking.status}\
                            and the new status is {status}'

        elif booking.status == 'Confirmed':
            if status == 'Finished':
                serializer.validated_data['status'] = status
            else:
                error = True
                message = f'The status of the booking cannot be changed because its status is {booking.status}\
                            and the new status is {status}'
        else:
            # if status receivied is cancelled or finished
            error = True
            message = f'The status of the booking cannot be changed because its status is {booking.status}'

        if error:
            return Response({'error': message}, status=status_codes.HTTP_409_CONFLICT)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': message}, status=status_codes.HTTP_409_CONFLICT)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def ratings(self, request, pk=None):
        try:
            booking = Booking.objects.get(id=pk)
        except exceptions.ObjectDoesNotExist:
            return Response({'error': 'Location with ID provided does not exist'},
                            status=status_codes.HTTP_404_NOT_FOUND)

        if request.user != booking.user_id:
            return Response({'error': 'User unauthorized'})

        # Validate if the booking has rating. Only one rating is allowed by booking
        ratings = Rating.objects.filter(booking_id=booking.id)

        if len(ratings) > 1:
            return Response({'error': 'The booking already has rating'},
                            status=status_codes.HTTP_409_CONFLICT)

        data = request.data
        data['location_id'] = booking.location_id.id
        data['booking_id'] = booking.id
        data['rating_date'] = datetime.today()

        serializer = RatingModelSerializer(data=data)
        if serializer.is_valid():
            serializer.validated_data()
            serializer.save()
            return Response(serializer.data, status=status_codes.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serializer.errors, status=status_codes.HTTP_400_BAD_REQUEST)


class BookingLocationsViewSet(viewsets.ViewSet):
    """ViewSet for manage the bookings of locations
    """

    @action(detail=True, methods=['get', 'post'], permission_classes=[permissions.AllowAny])
    def bookings(self, request, pk=None):
        try:
            location = Location.objects.get(pk=pk)
        except exceptions.ObjectDoesNotExist:
            return Response({'error': 'Location with ID provided does not exist'})

        # Save new booking
        data = request.data
        data['location_id'] = location.pk
        data['user_id'] = request.user.id

        if request.method == 'POST':
            if request.user.is_anonymous:
                return Response({'error': 'It is necessary to login to perform this action'})

            serializer = BookingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status_codes.HTTP_400_BAD_REQUEST)

        if request.method == 'GET':
            user_bookings = Booking.objects.filter(location_id=data['location_id'])
            serializer = DatesBookingSerializer(data=user_bookings, many=True)
            serializer.is_valid()
            return Response(serializer.data)

class BookingUsersViewSet(viewsets.ViewSet):
    """ViewSet for manage the bookings of each user
    """

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated, OwnProfilePermission])
    def bookings(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            if request.user.id != user.id:
                return Response({'error': 'User bookings request are not allowed for this user'},
                                status=status_codes.HTTP_401_UNAUTHORIZED)
            user_bookings = Booking.objects.filter(user_id=request.user.id)
            if len(user_bookings) != 0:
                serializer = BookingSerializer(data=user_bookings, many=True)
                serializer.is_valid()
                return Response(serializer.data)
            else:
                return Response({'error': 'This user has no bookings registered'},
                                status=status_codes.HTTP_400_BAD_REQUEST)
        except exceptions.ObjectDoesNotExist:
            return Response({'error': 'User with ID provided does not exist'},
                            status=status_codes.HTTP_404_NOT_FOUND)
