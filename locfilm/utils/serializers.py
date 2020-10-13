from rest_framework import serializers
from locfilm.utils.models.countries import Country, City

class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    country_id = serializers.StringRelatedField()
    country = country_id

    class Meta:
        model = City
        fields = ['name', 'country_id', 'country']

