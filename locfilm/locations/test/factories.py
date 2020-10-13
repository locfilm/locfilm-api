import factory


class LocationFactory(factory.django.DjangoModelFactory):
    """ Location factory.
    Create locations samples with random data """
    class Meta:
        model = 'locations.Location'
        django_get_or_create = ('id',)

    # name = models.CharField('location name', max_length=40)
    # description = models.TextField('location description', max_length=2000)
    # address = models.CharField('local address', max_length=50)

    # contact_email = models.EmailField('contact email', max_length=30)
    # price = models.FloatField('location price', max_length=10, help_text='Daily cost of rent in USD')
    # phone_regex = RegexValidator(
    #     regex=r'^\+?\d{9,15}$',
    #     message="Phone number must be entered in the format : +999999999. Up to 15 digits allowed."
    # )
    # contact_phone = models.CharField(validators=[phone_regex], max_length=16)
    # main_image = models.ImageField(upload_to='locations/pictures',
    #                                verbose_name='Main picture of a location', null=True)

    # # Foreign Keys
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    # categories = models.ManyToManyField('locations.Category', through='locations.Group',
    #                                     through_fields=('location', 'category'))

    # # Geolocation

    # latitude = models.FloatField('latitude', max_length=20)
    # longitude = models.FloatField('longitude', max_length=20)

    # # Stats

    # is_active = models.BooleanField('active location', default=False,
    #                                 help_text='If active, can be listed for rent')
    # has_parking = models.BooleanField('parking', default=False, help_text='Location has parking space')
    # has_dressing_room = models.BooleanField('dressing room', default=False,
    #                                         help_text='Location has dressing room space')
    # has_bathroom = models.BooleanField('bathroom', default=False, help_text='Location has bathroom')
    # has_cattering = models.BooleanField('cattering',
    # default=False, help_text='Location has cattering space')
    # has_wifi = models.BooleanField('wifi', default=False, help_text='Location has wifi available')
    # is_verified = models.BooleanField('verified location', default=False,
    #                                   help_text='locations has to be verified before listed for rent')
