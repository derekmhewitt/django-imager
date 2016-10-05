# from django.views.generic.base import TemplateView
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import ProfileView

urlpatterns = [
    url(r'^$',
        login_required(ProfileView.as_view(template_name="imager_profile/profile_view.html")),
        name='profile_view')
]
