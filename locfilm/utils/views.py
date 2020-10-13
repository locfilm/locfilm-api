from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .models.countries import Country, City

from .serializers import CountrySerializer, CitySerializer

class CountryList(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def get_permissions(self):
        """ Set permissions based in actions."""
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class CityList(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_permissions(self):
        """ Set permissions based in actions."""
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
