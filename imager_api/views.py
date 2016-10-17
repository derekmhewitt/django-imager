from django.contrib.auth.models import User
from imager_images.models import Photo
from rest_framework import viewsets
from .serializers import UserSerializer, PhotoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Automatically provides 'list' and 'detail' views."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permissions_classes = (IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
