from django.views.generic.base import TemplateView
from imager_images.models import Photo, Album
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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
    'aperture',
    'description',
    'published',
    'is_public',
    'albums',
]
ALBUM_FORM_FIELDS = [
    'title',
    'description',
    'cover_photo',
    'published',
]


class LibraryView(TemplateView):
    template_name = 'imager_images/library_view.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super(LibraryView, self).get_context_data(**kwargs)
        context['all_albums'] = Album.objects.all().filter(user=current_user)
        context['all_photos'] = Photo.objects.all().filter(user=current_user)
        # import pdb; pdb.set_trace()
        return context


class PhotoCreate(CreateView):
    template_name = "imager_images/photo_create.html"
    model = Photo
    fields = PHOTO_FORM_FIELDS
    success_url = reverse_lazy('my_library')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PhotoCreate, self).form_valid(form)


class AlbumCreate(CreateView):
    template_name = "imager_images/album_create.html"
    model = Album
    fields = ALBUM_FORM_FIELDS
    success_url = reverse_lazy('my_library')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)
