""" Bookings admin."""

# Django
from django.contrib import admin

# Models
from locfilm.bookings.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Booking admin."""

    list_display = ('user_id','location_id','creation_date','start_date','end_date','observations',)
