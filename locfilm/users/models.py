""" User model """

import uuid

# Django
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.validators import RegexValidator

# DRF
from rest_framework.authtoken.models import Token

# Apps
from locfilm.utils.models import City
from phone_field import PhoneField

class User(AbstractUser):


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # city_id = models.ForeignKey(City, on_delete=models.PROTECT, blank=True)
    # identification_type_id = models.ForeignKey(primary_key=False)
    # idenfification = models.CharField()
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={'unique': 'The mail is already in use. It must be unique'},

        )
    # phone_regex = RegexValidator(
    #     regex=r'\+?1?\d{9,15]$',
    #     message="Phone number must be entered in the format : +999999999. Up to 15 digits allowed."
    # )
    phone = models.CharField( max_length=17, blank=True)

    address = models.CharField(max_length=250, blank=True)
    is_verified = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']


    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
