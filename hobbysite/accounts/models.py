from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """Profile model for user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
