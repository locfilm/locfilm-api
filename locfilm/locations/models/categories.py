""" Categories Model. """

# Django
from django.db import models


class Category(models.Model):
    """ Categories Model.

    Locations belong to categories to make Groups of locations.
    """
    parent_id = models.PositiveIntegerField()
    name = models.CharField(unique=True, blank=False, max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField( upload_to='locations/pictures', height_field=None, width_field=None, blank=True )

    def __str__(self):
        return self.name

