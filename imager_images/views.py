from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from imager_images.models import Photo, Album
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        album_paginator = Paginator(
            Album.objects.all().filter(user=current_user), 4)
        photo_paginator = Paginator(
            Photo.objects.all().filter(user=current_user), 4)
        page_album = self.request.GET.get('page_album')
        page_photo = self.request.GET.get('page_photo')
        try:
            all_albums = album_paginator.page(page_album)
        except PageNotAnInteger:
            all_albums = album_paginator.page(1)
        except EmptyPage:
            all_albums = album_paginator.page(album_paginator.num_pages)
        try:
            all_photos = photo_paginator.page(page_photo)
        except PageNotAnInteger:
            all_photos = photo_paginator.page(1)
        except EmptyPage:
            all_photos = photo_paginator.page(photo_paginator.num_pages)
        context['all_albums'] = all_albums
        context['all_photos'] = all_photos
        return context


class AlbumView(DetailView):
    template_name = 'imager_images/album_view.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        album = self.object
        album_photos = Photo.objects.all().filter(albums=album)
        photo_paginator = Paginator(
            Photo.objects.all().filter(albums=album), 4)
        page_photo = self.request.GET.get('page_photo')
        try:
            album_photos = photo_paginator.page(page_photo)
        except PageNotAnInteger:
            album_photos = photo_paginator.page(1)
        except EmptyPage:
            album_photos = photo_paginator.page(photo_paginator.num_pages)
        context['album'] = album
        context['album_photos'] = album_photos
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
