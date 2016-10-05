from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'profile_view.html'

    def get_context_data(self, request, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        
