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
from locfilm.utils.models.countries import City, Country
from locfilm.utils.models.identification_types import IdentificationType
from phone_field import PhoneField

class User(AbstractUser):
    """ Model that defines User for locfilm aplication """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    city_id = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)
    identification_type_id = models.ForeignKey(IdentificationType, on_delete=models.PROTECT, null=True)
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

    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',
        message="Phone number must be entered in the format : +999999999. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex],max_length=16)

    address = models.CharField(max_length=250, blank=True)
    is_verified = models.BooleanField(default=True)

    # Variable configurations
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']


    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
