""" Locations admin.""" 

# Django 
from django.contrib import admin

# Models
from locfilm.locations.models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """ Location admin.""" 

    list_display = ('name', 'owner', 'city', 'is_active', 'is_verified')
    search_fields = ('name', 'city')
    list_filter = (
        'is_active',
        'is_verified',
        'has_parking',
        'has_dressing_room',
        'has_bathroom',
        'has_cattering',
        'has_wifi'

    )