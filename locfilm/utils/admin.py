""" GEneral utilites admin."""

from django.contrib import admin

# Models.
from locfilm.utils.models.countries import Country, City
from locfilm.utils.models.identification_types import IdentificationType

@admin.register(City)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

@admin.register(Country)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_editable = ('name',)
    list_filter = ('name',)

@admin.register(IdentificationType)
class IdTypesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_editable = ('name',)
    list_filter = ('name',)
