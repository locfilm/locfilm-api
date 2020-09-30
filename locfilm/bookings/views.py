
# DRF
from rest_framework import viewsets

# App data
from locfilm.bookings.serializers import BookingSerializer
from locfilm.bookings.models import Booking

# create a viewset
class BookingViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Booking.objects.all()

    # specify serializer to be used
    serializer_class = BookingSerializer
