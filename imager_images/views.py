from django.views.generic.base import TemplateView
from imager_images.models import Photo, Album

PHOTO_FORM_FIELDS = [
    'file',
    'title',
    'height_field',
    'width_field',
    'latitude',
    'longitude',
    'camera',
    'lens',
    'focal_length',
    'shutter_speed',
    'appature',
    'description',
    'published',
    'is_public',
    'albums',
]
ALBUM_FORM_FIELDS = [
    'photo',
    'id',
    'user',
    'title',
    'description',
    'cover_photo',
    'date_created',
    'date_modified',
    'date_pub',
    'published',
]


class LibraryView(TemplateView):
    template_name = 'imager_images/library_view.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super(LibraryView, self).get_context_data(**kwargs)
        context['all_albums'] = Album.objects.all().filter(user=current_user)
        context['all_photos'] = Photo.objects.all().filter(user=current_user)
        return context

# class PhotoCreate(CreateView):
#     model = Photo
#     fields = ['name']
