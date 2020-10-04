
# DRF
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Python
from datetime import date

# App data
from locfilm.bookings.serializers import BookingSerializer, DatesBookingSerializer
from locfilm.bookings.models import Booking
from locfilm.locations.models import Location
from locfilm.users.models import User
from locfilm.bookings.permissions import IsOwner, IsAllowed, OwnProfilePermission
from locfilm.locations.serializers.ratings import RatingModelSerializer



class BookingViewSet(viewsets.ModelViewSet):
    # specify serializer to be used
    serializer_class = BookingSerializer

    def get_queryset(self):
        """
        """
        queryset = Booking.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(booking__username=username)
        return queryset

    @action(detail=True,methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def ratings(self,request,pk=None):
        try:
            booking = Booking.objects.get(id=pk)
        except:
            return Response( {'error':'Location with ID provided does not exist'} )

        if request.user.id != booking.user_id:
            return Response({'error':'User unauthorized'})

        data = request.data
        data['location_id'] = booking.location_id
        data['booking_id'] = booking.id
        data['rating_date'] = date.today()

        serializer = RatingModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response( serializer.errors )


class BookingLocationsViewSet(viewsets.ViewSet):
    """ViewSet for manage the bookings of locations
    """

    @action(detail=True, methods=['get','post'], permission_classes=[permissions.AllowAny])
    def bookings(self, request, pk=None):
        try:
            location = Location.objects.get(pk=pk)
        except:
            return Response( {'error':'Location with ID provided does not exist'} )

        # Save new booking
        data = request.data
        data['location_id'] = location.pk
        data['user_id'] = request.user.id

        if request.method == 'POST':
            if request.user.is_anonymous:
                return Response({'error':'It is necessary to login to perform this action'})

            serializer = BookingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response( serializer.errors )

        if request.method == 'GET':
            user_bookings = Booking.objects.filter(location_id=data['location_id'])
            serializer =  DatesBookingSerializer(data=user_bookings, many=True)
            serializer.is_valid()
            return Response(serializer.data)

        #serializer =
class BookingUsersViewSet(viewsets.ViewSet):
    """ViewSet for manage the bookings of each user
    """

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated, OwnProfilePermission])
    def bookings(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            if request.user.id != user.id:
                return Response({'error':'User bookings request are not allowed for this user'})
            try:
                user_bookings = Booking.objects.filter(user_id=request.user.id)
                serializer =  BookingSerializer(data=user_bookings, many=True)
                serializer.is_valid()
                return Response(serializer.data)
            except:
                return Response({'error':'This user has no bookings registered'})
        except:
            return Response( {'error':'User with ID provided does not exist'} )
