from .views import CountryList, CityList
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'utils/cities', CityList, basename='city')
router.register(r'utils/countries', CountryList, basename='country')


urlpatterns = [
    path('', include(router.urls)),
]
