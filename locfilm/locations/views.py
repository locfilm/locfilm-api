""" Location views."""

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Serializers
from locfilm.locations.serializers import LocationSerializer

# Models
from locfilm.locations.models import Location


@api_view(['GET'])
def list_locations(request):
    """ List locations if active. """
    locations = Location.objects.filter(is_active=True)
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)




