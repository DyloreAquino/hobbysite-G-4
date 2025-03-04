from django.db import models

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() # from https://www.geeksforgeeks.org/textfield-django-models/

    class Meta:
        ordering = ['name'] # Order by name in ascending order




