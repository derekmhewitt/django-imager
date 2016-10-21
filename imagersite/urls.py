from django.conf.urls import include, url
from django.contrib import admin
from .views import index_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index_view, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),  # Note 1
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^images/', include('imager_images.urls')),
    url(r'^api/', include('imager_api.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
