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

    serializer_class = RatingModelSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Restrict list to verified only."""
        queryset = Rating.objects.all()

        return queryset
