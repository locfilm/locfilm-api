""" Locations urls. """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import locations as location_views

router = DefaultRouter()
router.register(r'locations', location_views.LocationViewSet, basename='location')

urlpatterns = [
    path('', include(router.urls))
]
