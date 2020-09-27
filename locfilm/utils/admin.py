""" GEneral utilites admin.""" 

from django.contrib import admin

# Models.
from locfilm.utils.models.countries import Country, City
from locfilm.utils.models.identificationtypes import IdentificationType

@admin.register(Country)
@admin.register(IdentificationType)

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class CountriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_editable = ('name',)
    list_filter = ('name',)

class IdTypesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_editable = ('name',)
    list_filter = ('name',)