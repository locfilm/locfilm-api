from django.urls import include, path
from rest_framework import routers

from locfilm.bookings import views

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingViewSet)
router.register(r'locations', views.BookingLocationsViewSet, basename='locations')
# /locations/<id>/bookings/
#router.register(r'^locations/{}$', views.BookingLocationsViewSet)
# /users/id/bookings/

#location_booking = views.BookingLocationsViewSet.as_view({'get':'retrieve'})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

    ]
