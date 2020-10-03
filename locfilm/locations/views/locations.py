""" Location views. """

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action


# Models
from locfilm.locations.models import Location

# Serializers
from locfilm.locations.serializers import LocationModelSerializer

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated


class LocationViewSet(viewsets.ModelViewSet):
    """ Location viewset. """

    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer

    def get_permissions(self):
        """ Set permissions based in actions."""
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]









