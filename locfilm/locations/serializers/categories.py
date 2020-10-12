""" Images serializer """

# DRF
from rest_framework import serializers

# Model
from locfilm.locations.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
