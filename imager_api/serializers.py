from rest_framework import serializers
from imager_images.models import Photo
from django.contrib.auth.models import User


class PhotoSerializer(serializers.Serializer):
    """Serialize some photos"""
    class Meta:
        model = Photo
        fields = ('url', 'user', 'albums', 'file', 'title', 'height_field',
                  'width_field', 'latitude', 'longitude', 'camera', 'lens',
                  'focal_length', 'shutter_speed', 'aperture', 'description',
                  'date_created', 'date_modified', 'published', 'is_public')

    def create(self, validated_data):
        """Create and return a new Photo, given validated data."""
        return Photo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Photo instance, given
        validated data."""
        instance.title = validated_data.get('title', instance.title)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize some users"""
    photos = serializers.HyperlinkedRelatedField(
        many=True, view_name='photo_detail', read_only=True
    )

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'photos')
