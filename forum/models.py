from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available")

    class Meta:
        ordering = ['name']
        verbose_name = 'Thread Category'
        verbose_name_plural = 'Thread Categories'

    def __str__(self):
        return str(self.name)


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='threads'
    )
    category = models.ForeignKey(
        ThreadCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='threads'
    )
    entry = models.TextField()
    image = models.ImageField(null=True, upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('forum:thread-detail', args=[self.pk])

    def get_edit_url(self):
        return reverse('forum:thread-update', args=[self.pk])


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='forum_comments'
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        null=False,
        related_name='forum_comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return str(self.entry)
