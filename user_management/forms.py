from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """A class for editing the profile's display name through a form."""

    class Meta:
        model = Profile
        fields = ['display_name',]