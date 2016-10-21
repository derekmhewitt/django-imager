from django.conf.urls import url, include
from .views import PhotoViewSet, UserViewSet, AlbumViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'photos', PhotoViewSet)
router.register(r'users', UserViewSet)
router.register(r'albums', AlbumViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
