""" Booking models """


from django.db import models


from locfilm.users.models import User
from locfilm.locations.models.locations import Location

class Booking(models.Model):
    """ Booking model.
        A booking consists in a reservation of a film location
    """

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now=True)

    # status = models.

    start_date = models.DateTimeField(verbose_name='Beggining of booking')
    end_date = models.DateTimeField(verbose_name='End of booking')

    # film_type = models.

    observations = models.TextField()

    def get_duration(self):
        pass
