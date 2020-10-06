""" Booking models """


from django.db import models


from locfilm.users.models import User
from locfilm.locations.models.locations import Location
from locfilm.config import common as settings

class Booking(models.Model):
    """ Booking model.
        A booking consists in a reservation of a film location
    """
<<<<<<< HEAD
    BOOKING_STATES = ['Pending','Confirmed','Cancelled','Finished']
=======
    BOOKING_STATES = [('Pending','Pending'), ('Confirmed','Confirmed',) ,('Cancelled','Cancelled',) ,('Finished','Finished',) ]
>>>>>>> migrations_new_server

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now=True)

<<<<<<< HEAD
    status = models.models.CharField(null=False,verbose_name='Status fo the booking', choices=BOOKING_STATES, default='Pending')
=======
    status = models.CharField(max_length=12, null=False,verbose_name='Status fo the booking', choices=BOOKING_STATES, default='Pending')
>>>>>>> migrations_new_server

    start_date = models.DateTimeField(verbose_name='Beggining of booking')
    end_date = models.DateTimeField(verbose_name='End of booking')

    # film_type = models.

    observations = models.TextField()

    def get_duration(self):
        pass

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
