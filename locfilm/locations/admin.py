""" Locations admin."""

# Django
from django.contrib import admin

# Models
from locfilm.locations.models import AdditionalInfo, Image, Location, Rating, Category, Group

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """ Location admin."""

    list_display = ('name', 'owner', 'city', 'is_active', 'is_verified', 'get_country')
    search_fields = ('name', 'city__name', 'city__country_id__name')
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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Category location admin."""

    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """ Category location admin."""

    list_display = ('location', 'category')
    search_fields = ('location', 'category')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """ Image location admin."""

    list_display = (
        'location_id',
        'booking_id',
        'rating_date',
        'accesibility',
        'conditions',
        'average',
        'description',
    )
