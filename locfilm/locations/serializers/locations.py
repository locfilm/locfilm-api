""" Locations serializer. """

# Django REST Framework
from rest_framework import serializers

# Model
from locfilm.locations.models import Location

class LocationModelSerializer(serializers.ModelSerializer):
    """Location model serializer. """

    class Meta:
        """ Meta class. """

        model = Location
        fields = (
            'id', 'name', 'address', 'contact_email', 'price', 'contact_phone',
            'owner', 'city', 'categories',
            'latitude', 'longitude', 'is_active', 'is_verified',
            'has_parking', 'has_dressing_room', 'has_bathroom', 'has_cattering', 'has_wifi',
            'main_image',
        )