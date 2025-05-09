from django.shortcuts import render
from django.views.generic.edit import UpdateView

from .models import Profile
from .forms import ProfileForm


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'username.html'
    
    slug_field = 'user__username'
    slug_url_kwarg = 'user__username'
    
    success_url = "/"

    form_class = ProfileForm
