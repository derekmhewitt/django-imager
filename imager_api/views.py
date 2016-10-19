from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from rest_framework import viewsets
from .serializers import UserSerializer, PhotoSerializer, AlbumSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Automatically provides 'list' and 'detail' views."""
    permissions_classes = (IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    permissions_classes = (IsAuthenticated,
                           IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AlbumViewSet(viewsets.ModelViewSet):
    permissions_classes = (IsAuthenticated,
                           IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
