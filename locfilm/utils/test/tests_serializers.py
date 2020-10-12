from django.test import TestCase
from nose.tools import eq_, ok_
from ..serializers import CountrySerializer, CitySerializer
from ..models.countries import Country

class TestCreateCountrySerializer(TestCase):

    def setUp(self):
        self.country_data = {
            "name": "Wonderland"
        }

    def test_serializer_with_empty_data(self):
        serializer = CountrySerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CountrySerializer(data=self.country_data)
        ok_(serializer.is_valid(), msg=serializer.errors)


class TestCreateCitySerializer(TestCase):

    def setUp(self):
        self.country = Country(name='Wonderland')
        self.country.save()
        self.city_data = {
            "name": "Gotaham",
            "country_id": self.country.pk,
        }

    def test_serializer_with_empty_data(self):
        serializer = CitySerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CitySerializer(data=self.city_data)
        ok_(serializer.is_valid(), msg=serializer.errors)
