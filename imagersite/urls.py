from django.conf.urls import include, url
from django.contrib import admin
from .views import index_view

urlpatterns = [
    url(r'^$', index_view, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.hmac.urls')),  # Note 1
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^images/', include('imager_images.urls')),
]
