from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """A class for creating profiles through a form."""

    class Meta:
        model = Profile
        fields = ['display_name',]