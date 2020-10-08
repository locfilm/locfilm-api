""" Aditional info model."""

# Django
from django.db import models

class AdditionalInfo(models.Model):
    """ Additional info

    To expand the detailes or new information regarding location.
    """
    location_id = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        """ Return location name"""
        return self.title
