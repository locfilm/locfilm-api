""" Locations urls. """

# Django
from django.urls import include, path


# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from locfilm.locations.views import list_locations

urlpatterns = [
    path('locations/', list_locations)
]
