from rest_framework import serializers
from imager_images import Photo

LANGUAGE_CHOICES = 'python'
STYLE_CHOICES = 'friendly'


class PhotoSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,
                                  allow_blank=True,
                                  max_length=100)
    code = serializers.CharField(
        style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(
        choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(
        choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """Create and return a new Photo, given validated data."""
        return Photo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Photo instance, given
        validated data."""
        instance.title = validated_data.get('title', instance.title)
