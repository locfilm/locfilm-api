import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from phone_field import PhoneField

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # city_id = models.ForeignKey(primary_key=False)
    # identification_type_id = models.ForeignKey(primary_key=False)
    # idenfification = models.CharField()
    # profile_pic = models.ImageField()

    email = models.CharField(max_length=250, unique=True)
    phone = PhoneField(default='0000000')

    address = models.CharField(max_length=250, blank=True)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
