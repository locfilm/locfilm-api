import factory
from django.core.files.base import ContentFile


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
    phone = factory.Sequence(lambda n: '123-555-%04d' % n)
    picture = factory.LazyAttribute(lambda _: ContentFile(
                                    factory.django.ImageField()._make_data({'width': 1024, 'height': 768}),
                                    'example.jpg'))
