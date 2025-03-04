from django.db import models

from datetime import datetime as dt

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() # from https://www.geeksforgeeks.org/textfield-django-models/

    class Meta:
        ordering = ['name'] # Order by name in ascending order


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='wiki_list'
    )
    entry = models.TextField()
    # Auto_now on DateTimeField from https://www.geeksforgeeks.org/datetimefield-django-models/
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']


