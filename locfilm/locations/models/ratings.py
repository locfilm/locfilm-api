# Django
from django.db import models

class Rating(models.Model):
    """Rating model
       A ranting consist in a evaluation of level of satisfatiction of the customer about the
       quality of the booking
    """

    location_id = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    booking_id = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE)
    rating_date = models.DateTimeField(verbose_name='Rating date')
    accesibility = models.IntegerField(verbose_name='Accesibility of location'),
    conditions= models.IntegerField(verbose_name='Conditions of location'),
    average = models.IntegerField(verbose_name='value for money of the location'),
    description= models.CharField(max_length=2000)

