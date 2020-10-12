# from django.test import TestCase
# from nose.tools import eq_, ok_
# from locfilm.locations.test.factories import LocationFactory
# from ..serializers import BookingSerializer
# from ..models import Booking, Location


# class TestBookingSerializer(TestCase):

#     def setUp(self):
#         self.country_data = {
#             "name": "Wonderland"
#         }

#     def test_serializer_with_empty_data(self):
#         serializer = BookingSerializer(data={})
#         eq_(serializer.is_valid(), False)

#     def test_serializer_with_valid_data(self):
#         serializer = BookingSerializer(data=self.country_data)
#         ok_(serializer.is_valid(), msg=serializer.errors)

#     def test_booking_creation_with_anonymous_user(self):
#         pass

#     def test_creation_booking_with_different_user(self):
#         """ Test a creation of booking with a different user than the logged """
#         pass
