""" Bookings serializers """

# DRF
from rest_framework import serializers
from locfilm.bookings.models import Booking
from datetime import date

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user_id', 'location_id', 'start_date', 'end_date', 'observations']

    # def validate_start_date(self, start_date):
    #     today = date.today()
    #     if start_date < today:
    #         raise serializers.ValidationError('You have to introduce a start day in the present or in the future')
    #     return start_date

    # def validate_end_date(self, start_date, end_date):

    #     pass
    # def create(self):
    #     pass

class BookingListSerializer(serializers.ListSerializer):
    """ Serializer to list all the Bookings of a specific user. """
    pass
