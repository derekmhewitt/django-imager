from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Photo, Album
from django.http import request

from .views import PHOTO_FORM_FIELDS, ALBUM_FORM_FIELDS, PhotoCreate

urlpatterns = [
    url(r'^$',
        login_required(TemplateView.as_view(
            template_name="imager_images/library.html")),
        name='my_library'),
    url(r'^photo/create/$',
        login_required(PhotoCreate.as_view()),
        name='photo_create'),
    url(r'^photo/edit/(?P<pk>[0-9]+)/$',
        login_required(UpdateView.as_view(
            template_name="imager_images/photo_edit.html",
            model=Photo,
            fields=PHOTO_FORM_FIELDS)),
        name='photo_edit'),
    url(r'^photo/delete/(?P<pk>[0-9]+)/$',
        login_required(DeleteView.as_view(
            template_name="imager_images/photo_delete.html",
            model=Photo)),
        name='photo_delete'),
    url(r'^album/create/$',
        login_required(CreateView.as_view(
            template_name="imager_images/album_create.html",
            model=Album,
            fields=ALBUM_FORM_FIELDS)),
        name='album_create'),
    url(r'^album/edit/(?P<pk>[0-9]+)/$',
        login_required(UpdateView.as_view(
            template_name="imager_images/album_edit.html",
            model=Album,
            fields=ALBUM_FORM_FIELDS)),
        name='album_edit'),
    url(r'^album/delete/(?P<pk>[0-9]+)/$',
        login_required(DeleteView.as_view(
            template_name="imager_images/album_delete.html",
            model=Album)),
        name='album_delete'),
]
