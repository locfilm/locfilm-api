""" Location Images model. """

# Django
from django.db import models


class Image(models.Model):
    """ Location Image model.

    Table to index the url required for media storage.
    """

    location_id = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        """ Return image name"""
        return self.title
