from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Photo


urlpatterns = [
    url(r'^$',
        login_required(TemplateView.as_view(template_name="imager_images/library.html")),
        name='my_library'),
    url(r'^photo/create/$',
        login_required(CreateView.as_view(template_name="imager_images/photo_create.html")),
        name='photo_create', model=Photo),
    url(r'^photo/edit/(?P<pk>[0-9]+)/$',
        login_required(UpdateView.as_view(template_name="imager_images/photo_edit.html")),
        name='photo_edit'),
    url(r'^photo/delete/(?P<pk>[0-9]+)/$',
        login_required(DeleteView.as_view(template_name="imager_images/photo_delete.html")),
        name='photo_delete'),
]
