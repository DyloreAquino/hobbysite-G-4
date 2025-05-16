from django import forms
from .models import Article, Comment, ArticleImage


class ArticleForm(forms.ModelForm):
    """
    A form for articles
    """
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            profile = user.profile
            self.fields['author'].initial = profile
            self.fields['author'].disabled = True


class ArticleUpdateForm(forms.ModelForm):
    """
    A form for updating articles
    """
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['author']


class CommentForm(forms.ModelForm):
    """
    A form for comments
    """
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['author', 'article']


class ArticleImageForm(forms.ModelForm):
    """
    A form for article images
    """
    class Meta:
        model = ArticleImage
        fields = '__all__'
        exclude = ['author', 'article']
