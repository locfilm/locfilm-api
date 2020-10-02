""" Bookings serializers """

# DRF
from rest_framework import serializers
from locfilm.bookings.models import Booking
from datetime import date

class BookingSerializer(serializers.ModelSerializer):
    """Booking Serializer
    """
    #user_id = serializers.StringRelatedField()
    #location_id = serializers.StringRelatedField()
    class Meta:
        model = Booking
        fields = ['user_id', 'location_id', 'start_date', 'end_date', 'observations']


    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("finish must occur after start")

        return data

class BookingListSerializer(serializers.ListSerializer):
    """ Serializer to list all the Bookings of a specific user. """
    pass
