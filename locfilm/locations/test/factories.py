
# Factories
from locfilm.utils.test.factories import CityFactory
from locfilm.users.test.factories import UserFactory

# Libraries
import factory
from faker import Factory

faker = Factory.create()

class LocationFactory(factory.django.DjangoModelFactory):
    """ Location factory.
    Create locations samples with random data """
    class Meta:
        model = 'locations.Location'

    name = faker.name()
    description = faker.text()

    price = faker.pyint()
    address = faker.address()
    contact_email = faker.email()
    contact_phone = faker.phone_number()
    main_image = faker.image_url()

    # # Foreign Keys
    owner = factory.SubFactory(UserFactory)
    city = factory.SubFactory(CityFactory)
    # categories = models.ManyToManyField('locations.Category', through='locations.Group',
    #                                     through_fields=('location', 'category'))

    # # Geolocation
    latitude = faker.latitude()
    longitude = faker.longitude()

    # # Stats

    is_active = faker.pybool()
    has_parking = faker.pybool()
    has_dressing_room = faker.pybool()
    has_bathroom = faker.pybool()
    has_cattering = faker.pybool()
    has_wifi = faker.pybool()
    is_verified = faker.pybool()
