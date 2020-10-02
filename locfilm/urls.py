from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

# Urls from apps
from .heros.urls import urlpatterns as HeroUrls
from .users.urls import urlpatterns as UserUrls

root = ''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('locfilm.heros.urls', 'heros'), namespace='heros')),
    path('', include(('locfilm.users.urls', 'users'), namespace='users')),
    path('', include(('locfilm.locations.urls', 'locations'), namespace='locations')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
