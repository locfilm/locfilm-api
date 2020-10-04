""" Ratings serializer """

# DRF
from rest_framework import serializers

# Model
from locfilm.locations.models import Rating

class RatingModelSerializer(serializers.ModelSerializer):
    """ Rating model serializer. """
    class Meta:

        model = Rating
        fields = '__all__'
