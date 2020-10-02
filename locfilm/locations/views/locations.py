""" Location views. """

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from locfilm.locations.models import Location

# Serializers
from locfilm.locations.serializers import LocationModelSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """ Location viewset. """

    serializer_class = LocationModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Restrict list to verified only."""
        queryset = Location.objects.all()
        if self.action == 'list':
            return queryset.filter(is_verified=True)
        return queryset


