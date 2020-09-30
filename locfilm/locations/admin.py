""" Locations admin."""

# Django
from django.contrib import admin

# Models
from locfilm.locations.models import Location
from locfilm.locations.models import AdditionalInfo
from locfilm.locations.models import Image

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

@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    """ Additional Info admin."""

    list_display = ('location_id', 'title')
    search_fields = ('location_id', 'title')

@admin.register(Image)
class ImageLocationAdmin(admin.ModelAdmin):
    """ Image location admin."""

    list_display = ('location_id', 'title')
    search_fields = ('location_id', 'title')
