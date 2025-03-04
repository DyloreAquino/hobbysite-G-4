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
    # Assistance from https://stackoverflow.com/questions/56310322/django-datetimefield-with-auto-now-add-asks-for-default
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']


