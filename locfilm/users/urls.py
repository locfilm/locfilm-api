from .views import UserViewSet, UserCreateViewSet, hello_world, CustomObtainAuthToken
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken import views as AuthView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/hi', hello_world),
    path('users/api-token-auth/', AuthView.obtain_auth_token),
    path('users/login', CustomObtainAuthToken.as_view()),

]
