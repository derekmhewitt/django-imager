from django.views.generic.base import TemplateView
from imager_images.models import Photo, Album


class ProfileView(TemplateView):
    template_name = 'imager_profile/profile_view.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['num_albums'] = len(Album.objects.all().filter(user=current_user))
        context['four_albums'] = Album.objects.all().filter(user=current_user)[:4]
        context['num_photos'] = len(Photo.objects.all().filter(user=current_user))
        context['four_photos'] = Photo.objects.all().filter(user=current_user)[:4]
        return context
