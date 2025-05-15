from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    title = models.CharField(max_length=255)

    author = models.ForeignKey(Profile,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='articles')

    category = models.ForeignKey(ArticleCategory,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='articles')
    entry = models.TextField()
    header_image = models.ImageField(upload_to='images/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.pk])

    def get_edit_url(self):
        return reverse('blog:article_update', args=[self.pk])


class Comment(models.Model):
    author = models.ForeignKey(Profile,
                               on_delete=models.SET_NULL,
                               null=True,)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name='comments')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return str(self.entry)


class ArticleImage(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True)

    article = models.ForeignKey(Article,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='images')

    def __str__(self):
        return f'{self.description}'
