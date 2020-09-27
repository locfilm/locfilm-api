from rest_framework.views import APIView
from rest_framework.response import Response

from .models.countries import Country, City

from .serializers import CountrySerializer, CitySerializer

class CountryList(APIView):
    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

class CityList(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)