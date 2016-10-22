from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from rest_framework import viewsets
from .serializers import UserSerializer, PhotoSerializer, AlbumSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Automatically provides 'list' and 'detail' views."""
    permission_classes = (IsAuthenticated,
                          IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,
                          IsOwnerOrReadOnly,)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,
                          IsOwnerOrReadOnly,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
