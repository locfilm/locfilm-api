from django.urls import include, path
from rest_framework import routers

from locfilm.bookings import views


router = routers.DefaultRouter()
router.register(r'bookings', views.BookingViewSet, basename='bookings')
router.register(r'locations', views.BookingLocationsViewSet, basename='locations')
router.register(r'users', views.BookingUsersViewSet, basename='users')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path('', include(router.urls))]
