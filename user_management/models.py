from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model for user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=63, blank=False)
    email_address = models.EmailField()
    
    def __str__(self):
        return str(self.display_name)
