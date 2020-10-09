# Create new objects in db

from locfilm.users.models import User
from django.forms.models import model_to_dict

from locfilm.users.test.factories import UserFactory
from locfilm.users.serializers import CreateUserSerializer

for i in range(200):
    # Crear un nuevo usuario del faker
    new_user = model_to_dict(UserFactory.build())

    # Serializer
    serializer = CreateUserSerializer(data=new_user)
    print(new_user)
    # Agregar usuario a BD con Serializer
    if serializer.is_valid():
        serializer.save()


# # Crear locaciones
# for i in nuevo usuario del faker
#     new_location = n range(100):
#     # Crear umodel_to_dict(UserFactory.build())
#     new_location_id = new_location.id

#     # Crear images
#     for i in range(10):
#         new_image = image_fake.build(location_id=new_location_id)


#     # Serializer
#     serializer = CreateUserSerializer(data=self.user_data)

#     # Agregar usuario a BD con Serializer
#     serializer.is_valid()
#     serializer.create()
