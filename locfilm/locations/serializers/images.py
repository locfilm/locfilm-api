""" Images serializer """

# DRF
from rest_framework import serializers

# Model
from locfilm.locations.models import Image

class ImageModelSerializer(serializers.ModelSerializer):
    """ Image model serializer. """
    class Meta:

        model = Image
        fields = '__all__'
