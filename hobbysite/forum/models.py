from django.db import models
from django.urls import reverse

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available")

    class Meta:
        ordering = ['name'] # Order by name in ascending order
    
    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.SET_NULL,
        null=True,
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on'] # Order by name in ascending order
    
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('forum:post-detail', args=[self.pk])