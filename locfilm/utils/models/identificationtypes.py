""" Identification types models """

from django.db import models

class IdentificationType(models.Model):
    name = models.CharField("Identification name", max_length = 50)

    def __str__(self):
        return self.name