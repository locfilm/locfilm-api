""" Locations model."""

# Django
from django.db import models

class Location (models.Model):
    """ Location model.

    A location is owned and rented by different users. Bookings are managed, created, updated and deleted by Admin. 
    """ 

    name = models.CharField('location name', max_length=40)
    description = models.TextField('location description', max_length=2000)
    address = models.CharField('local address', max_length=50)
            
    contact_phone = models.TextField('contact phone', max_length=20)
    contact_email = models.EmailField('contact email', max_length=30)
    price = models.FloatField('location price', max_length=10)
    
    # Foreign Keys

    owner = models.CharField('owner name', max_length=50)
    city = models.CharField('city', max_length=50)
    aditional_info = models.CharField('aditional info', max_length=200)
    locations_images = models.ImageField('location pictures', upload_to='location/pictures/', blank=True, null=True, height_field=None, width_field=None, max_length=None)

    # Geolocation

    latitude = models.FloatField('latitude', max_length=20)
    longitude = models.FloatField('longitude', max_length=20)

    # Stats

    is_active = models.BooleanField('active location', default=False, help_text='If active, can be listed for rent')
    has_parking = models.BooleanField('parking', default=False, help_text='Location has parking space')
    has_dressing_room = models.BooleanField('dressing room', default=False, help_text='Location has dressing room space')
    has_bathroom = models.BooleanField('bathroom', default=False, help_text='Location has bathroom')
    has_cattering = models.BooleanField('cattering', default=False, help_text='Location has cattering space')
    has_wifi = models.BooleanField('wifi', default=False, help_text='Location has wifi available')
    is_verified = models.BooleanField('verified location', default=False, help_text='locations has to be verified before listed for rent')
    
    def __str__(self):
        """ Return Location name."""
        return self.name
    