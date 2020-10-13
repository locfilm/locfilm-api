""" Location categories views. """

# Django REST Framework
from rest_framework import viewsets

# Models
from locfilm.locations.models import Category

# Serializers
from locfilm.locations.serializers.categories import CategorySerializer

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated


class CategoriesViewSet(viewsets.ModelViewSet):
    """ Categories viewset. """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        """ Set permissions based in actions."""
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
