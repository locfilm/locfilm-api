""" Images from locations views. """

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from locfilm.locations.models import Image

# Serializers
from locfilm.locations.serializers.images import ImageModelSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    """ Images viewset. """

    serializer_class = ImageModelSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Restrict list to verified only."""
        queryset = Image.objects.all()

        return queryset
