from rest_framework import serializers
from locfilm.utils.models.countries import Country, City

class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = City
        fields = '__all__'
