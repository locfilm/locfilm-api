""" Ratings views. """


# Django REST Framework
from rest_framework import viewsets

# Models
from locfilm.locations.models import Rating

# Serializers
from locfilm.locations.serializers import RatingModelSerializer

class RatingViewSet(viewsets.ModelViewSet):
    """ Rating viewset. """

    serializer_class = RatingModelSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Restrict list to verified only."""
        queryset = Rating.objects.all()

        return queryset
