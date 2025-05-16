from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User
from .forms import UserForm

from user_management.models import Profile

class UserCreateView(CreateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserForm
    success_url = '/'
    
    def form_valid(self, form):
        user = form.save()
        user.profile = Profile()
        user.profile.display_name = user.username
        user.profile.email_address = user.email
        user.profile.save()
        login(self.request, user)
        return super().form_valid(form)