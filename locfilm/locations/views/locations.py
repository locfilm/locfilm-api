""" Location views. """

# Django
from django.core import exceptions

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from locfilm.locations.models import Location, Image, Rating

# Serializers
from locfilm.locations.serializers import LocationModelSerializer, ImageModelSerializer, RatingModelSerializer

# Permissions

class LocationViewSet(viewsets.ModelViewSet):
    """ Location viewset. """

    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer

    def get_permissions(self):
        """ Set permissions based in actions."""
        if self.action in ['list', 'images', 'ratings']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['get'], permission_classes=[AllowAny], url_name='location-images')
    def images(self, request, pk=None):
        """ View to return all the images of a specific location """
        try:
            location = Location.objects.get(id=pk)
            print(location)
        except exceptions.ObjectDoesNotExist:
            return Response({'error': 'This locations does not exist'})

        queryset = Image.objects.filter(location_id=pk)
        serializer = ImageModelSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[AllowAny])
    def ratings(self, request, pk=None):
        try:
            Location.objects.get(id=pk)
        except exceptions.ObjectDoesNotExist:
            return Response({'error': 'Location with ID provided does not exist'})

        rating_locations = Rating.objects.filter(location_id=pk)
        serializer = RatingModelSerializer(data=rating_locations, many=True)
        serializer.is_valid()
        return Response(serializer.data)
