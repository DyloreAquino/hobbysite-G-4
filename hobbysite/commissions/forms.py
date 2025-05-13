from django import forms

from .models import Commission, Job


class CommissionAddForm(forms.ModelForm):
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


class JobAddForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
