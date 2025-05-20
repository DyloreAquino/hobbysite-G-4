from django.shortcuts import render


from django.contrib.auth.models import User
from user_management.models import Profile


def homepage(request):
    context = {}

    for user in User.objects.all():
        if not hasattr(user, 'profile'):
            user.profile = Profile()
            user.profile.display_name = user.username
            user.profile.email_address = user.email
            user.profile.save()

    return render(request, 'homepage.html', context)
