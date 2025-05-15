from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    # from https://www.geeksforgeeks.org/textfield-django-models/
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Order by name in ascending order


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='wiki_articles'
    )
    entry = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:article-detail', args=[self.pk])

    def get_edit_url(self):
        return reverse('wiki:article-update', args=[self.pk])

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='wiki_comments'
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=True,
        related_name='wiki_comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']
