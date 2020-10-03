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
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("finish must occur after start")

        booking_locations = Booking.objects.filter(location_id=data['location_id'])
        booking_locations = filter(lambda l: (l.start_date >= data['start_date'] and l.start_date <= data['end_date'])\
                                 or (l.end_date >= data['end_date'] and l.end_date <= data['end_date']), booking_locations)
        if len(list(booking_locations)) != 0:
            raise serializers.ValidationError("The location is already booked in the selected dates")

        return data

class BookingListSerializer(serializers.ListSerializer):
    """ Serializer to list all the Bookings of a specific user. """

    class Meta:
        model = Booking
        fields = '__all__'
