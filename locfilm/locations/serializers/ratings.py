""" Ratings serializer """

# DRF
from rest_framework import serializers

# Model
from locfilm.locations.models import Rating

class RatingModelSerializer(serializers.ModelSerializer):
    """ Rating model serializer. """
    accesibility = serializers.IntegerField(required=True)
    conditions = serializers.IntegerField(required=True, help_text='Conditions of the location')
    average = serializers.IntegerField(required=True, help_text='General experience')
    class Meta:

        model = Rating
        fields = ('id','location_id','booking_id','rating_date','accesibility','conditions','average','description')
