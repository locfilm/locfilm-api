import factory


class LocationFactory(factory.django.DjangoModelFactory):
    """ Location factory.
    Create locations samples with random data """
    class Meta:
        model = 'locations.Location'
        django_get_or_create = ('id',)
