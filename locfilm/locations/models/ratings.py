# Django
from django.db import models

class Rating(models.Model):
    """Rating model
       A ranting consist in a evaluation of level of satisfatiction of the customer about the
       quality of the booking
    """
    RATINGS_CHOICES = ['1','2','3','4','5']

    location_id = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    booking_id = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE)
    rating_date = models.DateTimeField(verbose_name='Rating date')
    accesibility = models.CharField(null=False, verbose_name='Accesibility of location', choices= RATINGS_CHOICES, default=1),
    conditions = models.CharField(null=False, verbose_name='Conditions of location', choices= RATINGS_CHOICES, default=1),
    average = models.CharField(null=False, verbose_name='value for money of the location', choices= RATINGS_CHOICES, default=1),
    description = models.CharField(null=True, max_length=2000,verbose_name='Observations about the experience of the user')

