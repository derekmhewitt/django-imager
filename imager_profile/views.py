from django.views.generic.base import TemplateView
from imager_images.models import Photo, Album


class ProfileView(TemplateView):
    template_name = 'imager_profile/profile_view.html'

    def get_context_data(self, **kwargs):
        # import pdb; pdb.set_trace()
        current_user = self.request.user
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['num_albums'] = len(Album.objects.all().filter(user=current_user))
        context['five_albums'] = Album.objects.all().filter(user=current_user)[:5]
        context['num_photos'] = len(Photo.objects.all().filter(user=current_user))
        context['five_photos'] = Photo.objects.all().filter(user=current_user)[:5]
        return context
