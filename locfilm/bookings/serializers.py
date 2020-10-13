""" Bookings serializers """

# DRF
from rest_framework import serializers
from locfilm.bookings.models import Booking

# Models
from locfilm.locations.models import Location

class LocationFieldSerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'city', 'main_image']

class BookingSerializer(serializers.ModelSerializer):
    """Booking Serializer
    """

    class Meta:
        model = Booking
        fields = ['id', 'user_id', 'location_id', 'start_date', 'end_date', 'observations', 'status']

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("finish must occur after start")

        booking_locations = Booking.objects.filter(location_id=data['location_id'])
        booking_locations = filter(lambda l: (l.start_date >= data['start_date'] and l.start_date <= data[
            'end_date']) or (l.end_date >= data['end_date'] and l.end_date <= data['end_date']),
            booking_locations)
        if len(list(booking_locations)) != 0:
            raise serializers.ValidationError("The location is already booked in the selected dates")

        return data

class BookingListSerializer(serializers.ModelSerializer):
    """Booking Serializer
    """
    location_id = LocationFieldSerializer()
    # location = LocationFieldSerializer(instance=Location.objects.get(id=location_id.get_value)

    class Meta:
        model = Booking
        fields = ['id', 'user_id', 'location_id', 'start_date',
                  'end_date', 'observations', 'status']

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("finish must occur after start")

        booking_locations = Booking.objects.filter(location_id=data['location_id'])
        booking_locations = filter(lambda l: (l.start_date >= data['start_date'] and l.start_date <= data[
            'end_date']) or (l.end_date >= data['end_date'] and l.end_date <= data['end_date']),
            booking_locations)
        if len(list(booking_locations)) != 0:
            raise serializers.ValidationError("The location is already booked in the selected dates")

        return data

class DatesBookingSerializer(serializers.ModelSerializer):
    """ Serializer to list all the Bookings of locations with their dates """

    class Meta:
        model = Booking
        fields = ('location_id', 'start_date', 'end_date')


class UpdateBookingStatusSerializer(serializers.ModelSerializer):
    """ Serializer that update the status of a booking"""

    BOOKING_STATES = [('Pending', 'Pending'), ('Confirmed', 'Confirmed',),
                      ('Cancelled', 'Cancelled',), ('Finished', 'Finished',)]

    status = serializers.ChoiceField(required=True, choices=BOOKING_STATES, )

    class Meta:
        model = Booking
        fields = ['status']
