# Generated by Django 3.1.1 on 2020-10-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(verbose_name='Beggining of booking')),
                ('end_date', models.DateTimeField(verbose_name='End of booking')),
                ('observations', models.TextField()),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
