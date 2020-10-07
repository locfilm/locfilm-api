""" Groups model."""

# Django
from django.db import models


class Group (models.Model):
    """ Group model.

    A Group is the table that holds the relationship between
    Location and Category.
    """

    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    category = models.ForeignKey('locations.Category', on_delete=models.CASCADE)

    def __str__(self):
        """Return Location and Category"""
        return '{} at {}'.format(self.location, self.category)
