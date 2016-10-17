from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import PhotoViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'photos', PhotoViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^v1/$', login_required(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
