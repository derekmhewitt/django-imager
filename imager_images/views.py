from django.views.generic.base import TemplateView
from imager_images.models import Photo, Album


class LibraryView(TemplateView):
    template_name = 'imager_images/library_view.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super(LibraryView, self).get_context_data(**kwargs)
        context['all_albums'] = Album.objects.all().filter(user=current_user)
        context['all_photos'] = Photo.objects.all().filter(user=current_user)
        return context
