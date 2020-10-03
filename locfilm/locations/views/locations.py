""" Location views. """

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from locfilm.locations.models import Location, Image

# Serializers
from locfilm.locations.serializers import LocationModelSerializer, ImageModelSerializer

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

    @action(detail=True, methods=['get'],)
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
