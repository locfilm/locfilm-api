""" Location views. """

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from locfilm.locations.models import Location, Image

# Serializers
from locfilm.locations.serializers import LocationModelSerializer, ImageModelSerializer

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class LocationViewSet(viewsets.ModelViewSet):
    """ Location viewset. """

    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer

    # Filter
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'city__name']
    filter_fields = ['is_active', 'is_verified',
    'has_parking', 'has_dressing_room', 'has_bathroom', 'has_cattering', 'has_wifi']

    def get_permissions(self):
        """ Set permissions based in actions."""
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    @action(detail=True, methods=['get'], permission_classes=[AllowAny])
    def images(self, request, pk=None):
        """ View to return all the images of a specific location """
        try:
            location = Location.objects.get(id=pk)
            print(location)
        except:
            return Response({'error':'This locations does not exist' })

        queryset = Image.objects.filter(location_id=pk)
        serializer = ImageModelSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(serializer.data)
