""" Ratings serializer """

# DRF
from rest_framework import serializers

# Model
from locfilm.locations.models import Rating

class RatingModelSerializer(serializers.ModelSerializer):
    """ Rating model serializer. """
    class Meta:

        model = Rating
        fields = ('id','location_id','booking_id','rating_date','accesibility','conditions','average','description')
