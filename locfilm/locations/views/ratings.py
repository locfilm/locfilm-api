""" Ratings views. """

# Python
from datetime import date

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from locfilm.locations.models import Rating, Location
from locfilm.bookings.models import Booking

# Serializers
from locfilm.locations.serializers import RatingModelSerializer

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

class RatingViewSet(viewsets.ModelViewSet):
    """ Rating viewset. """

    @action(detail=True, methods=['get','post'], permission_classes=[permissions.AllowAny])
    def ratings(self, request, pk=None):
        try:
            location = Location.objects.get(pk=pk)
        except:
            return Response( {'error':'Location with ID provided does not exist'} )

        try:
            booking = Booking.objects.get(pk=pk)
        except:
            return Response( {'error':'Booking with ID provided does not exist'} )

        # Save new booking
        data = request.data
        data['location_id'] = location.pk
        data['booking_id'] = booking.pk

        if request.method == 'POST':
            if request.user.is_anonymous:
                return Response({'error':'It is necessary to login to perform this action'})

            data['rating_date'] = date.today()
            serializer = RatingModelSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response( serializer.errors )

        if request.method == 'GET':
            rating_locations = Rating.objects.filter(location_id=data['location_id'])
            serializer =  RatingModelSerializer(data=rating_locations, many=True)
            serializer.is_valid()
            return Response(serializer.data)
