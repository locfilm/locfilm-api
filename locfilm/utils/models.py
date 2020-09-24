""" Counturies and cities models """

from django.db import models

class Country(models.Model):
    name = models.CharField("Country name", max_length = 50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField("City name", max_length = 50)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
