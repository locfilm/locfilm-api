# Generated by Django 3.1.1 on 2020-10-03 20:06

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200927_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]