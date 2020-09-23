# Generated by Django 3.1.1 on 2020-09-23 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='location name')),
                ('description', models.TextField(max_length=2000, verbose_name='location description')),
                ('address', models.CharField(max_length=50, verbose_name='local address')),
                ('contact_phone', models.TextField(max_length=20, verbose_name='contact phone')),
                ('contact_email', models.EmailField(max_length=30, verbose_name='contact email')),
                ('price', models.FloatField(max_length=10, verbose_name='location price')),
                ('owner', models.CharField(max_length=50, verbose_name='owner name')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('aditional_info', models.CharField(max_length=200, verbose_name='aditional info')),
                ('locations_images', models.ImageField(blank=True, null=True, upload_to='location/pictures/', verbose_name='location pictures')),
                ('latitude', models.FloatField(max_length=20, verbose_name='latitude')),
                ('longitude', models.FloatField(max_length=20, verbose_name='longitude')),
                ('is_active', models.BooleanField(default=False, help_text='If active, can be listed for rent', verbose_name='active location')),
                ('has_parking', models.BooleanField(default=False, help_text='Location has parking space', verbose_name='parking')),
                ('has_dressing_room', models.BooleanField(default=False, help_text='Location has dressing room space', verbose_name='dressing room')),
                ('has_bathroom', models.BooleanField(default=False, help_text='Location has bathroom', verbose_name='bathroom')),
                ('has_cattering', models.BooleanField(default=False, help_text='Location has cattering space', verbose_name='cattering')),
                ('has_wifi', models.BooleanField(default=False, help_text='Location has wifi available', verbose_name='wifi')),
                ('is_verified', models.BooleanField(default=False, help_text='locations has to be verified before listed for rent', verbose_name='verified location')),
            ],
        ),
    ]
