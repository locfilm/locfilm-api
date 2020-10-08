""" Ratings serializer """

# DRF
from rest_framework import serializers

# Model
from locfilm.locations.models import Rating

class RatingModelSerializer(serializers.ModelSerializer):
    """ Rating model serializer. """
    CHOICES = [1, 2, 3, 4, 5]
    accesibility = serializers.ChoiceField(required=True, help_text='accesibility of the location. 1 to 5',
                                           choices=CHOICES)
    conditions = serializers.ChoiceField(required=True, help_text='Conditions of the location. 1 to 5',
                                         choices=CHOICES)
    average = serializers.ChoiceField(required=True, help_text='General experience. 1 to 5', choices=CHOICES)

    class Meta:
        model = Rating
        fields = ('id', 'location_id', 'booking_id', 'rating_date',
                  'accesibility', 'conditions', 'average', 'description')
