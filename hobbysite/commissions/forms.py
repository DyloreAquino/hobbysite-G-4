from django import forms

from .models import (Commission, 
                     Job,
                     JobApplication)


class JobAppForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []
        
class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            profile = user.profile
            self.fields['author'].initial = profile
            self.fields['author'].disabled = True


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['commission']
