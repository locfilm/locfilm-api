""" Location serializers. """

# Models
from locfilm.locations.models import Location

# Django REST Framework
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    """ Location Model Serializer."""

    class Meta:
        """ Meta class."""

        model = Location
        fields = '__all__'
