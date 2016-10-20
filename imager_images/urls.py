from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Photo, Album

from .views import PHOTO_FORM_FIELDS, ALBUM_FORM_FIELDS
from .views import PhotoCreate, AlbumCreate, LibraryView
from django.urls import reverse_lazy

urlpatterns = [
    url(r'^$',
        login_required(LibraryView.as_view(
            template_name="imager_images/library.html")),
        name='my_library'),
    url(r'^photo/create/$',
        login_required(PhotoCreate.as_view()),
        name='photo_create'),
    url(r'^photo/edit/(?P<pk>[0-9]+)/$',
        login_required(UpdateView.as_view(
            template_name="imager_images/photo_edit.html",
            model=Photo,
            fields=PHOTO_FORM_FIELDS,
            success_url=reverse_lazy('my_library'))),
        name='photo_edit'),
    url(r'^photo/delete/(?P<pk>[0-9]+)/$',
        login_required(DeleteView.as_view(
            template_name="imager_images/photo_delete.html",
            model=Photo,
            success_url=reverse_lazy('my_library'))),
        name='photo_delete'),
    url(r'^album/create/$',
        login_required(AlbumCreate.as_view()),
        name='album_create'),
    url(r'^album/edit/(?P<pk>[0-9]+)/$',
        login_required(UpdateView.as_view(
            template_name="imager_images/album_edit.html",
            model=Album,
            fields=ALBUM_FORM_FIELDS,
            success_url=reverse_lazy('my_library'))),
        name='album_edit'),
    url(r'^album/delete/(?P<pk>[0-9]+)/$',
        login_required(DeleteView.as_view(
            template_name="imager_images/album_delete.html",
            model=Album,
            success_url=reverse_lazy('my_library'))),
        name='album_delete'),
    url(r'album/(?P<pk>[0-9]+)/$',
        login_required(DetailView.as_view(
            template_name="imager_images/album_view.html",
            model=Album,)),
        name='album_view'),
    url(r'photos/(?P<pk>[0-9]+)/$',
        login_required(DetailView.as_view(
            template_name="imager_images/photo_view.html",
            model=Photo,)),
        name='photo_view'),
]
