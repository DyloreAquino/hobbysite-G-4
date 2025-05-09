from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model for user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.TextField(max_length=63, blank=False)
    email_address = models.EmailField(blank=False)
