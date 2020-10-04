""" Locations urls. """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import locations as location_views
from .views import images as image_views


router = DefaultRouter()
router.register(r'locations', location_views.LocationViewSet, basename='location')
router.register(r'images', image_views.ImagesViewSet, basename='images')

urlpatterns = [
    path('', include(router.urls))
]