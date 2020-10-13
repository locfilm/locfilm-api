from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from locfilm.users.urls import urlpatterns as UserUrls
from locfilm.bookings.urls import urlpatterns as BookingUrls
from locfilm.locations.urls import urlpatterns as LocationUrls
from locfilm.utils.urls import urlpatterns as UtilsUrls
root = ''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(UserUrls)),
    path('', include(BookingUrls)),
    path('', include(LocationUrls)),
    path('', include(UtilsUrls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
