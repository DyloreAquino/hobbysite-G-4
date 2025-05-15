from django import forms

from .models import Thread, Comment


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            profile = user.profile
            self.fields['author'].initial = profile
            self.fields['author'].disabled = True


class ThreadUpdateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        exclude = ['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['author', 'thread']
