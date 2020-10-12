import factory
from faker import Factory

faker = Factory.create()

class CountryFactory(factory.django.DjangoModelFactory):
    """ Country factory.
    Create locations samples with random data """
    class Meta:
        model = 'utils.Country'

    name = faker.country()


class CityFactory(factory.django.DjangoModelFactory):
    """ Country factory.
    Create locations samples with random data """
    class Meta:
        model = 'utils.City'

    name = faker.country()
    country_id = factory.SubFactory(CountryFactory)
