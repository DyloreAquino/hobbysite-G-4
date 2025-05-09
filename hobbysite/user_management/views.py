from django.shortcuts import render
from django.views.generic.edit import UpdateView

from .models import Profile
from .forms import ProfileForm

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'user_management/username.html'

    form_class = ProfileForm
