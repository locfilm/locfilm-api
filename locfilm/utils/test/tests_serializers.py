from django.test import TestCase
from nose.tools import eq_, ok_
from ..serializers import CountrySerializer


class TestCreateCountrySerializer(TestCase):

    def setUp(self):
        self.country_data = {
            "name": "Wonderland"
        }

    def test_serializer_with_empty_data(self):
        serializer = CountrySerializer(data={})
        eq_(serializer.is_valid(), True)

    def test_serializer_with_valid_data(self):
        serializer = CountrySerializer(data=self.country_data)
        ok_(serializer.is_valid(), msg=serializer.errors)
