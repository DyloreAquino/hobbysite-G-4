from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    # from https://www.geeksforgeeks.org/textfield-django-models/
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Order by name in ascending order
        verbose_name = 'article_category'
        verbose_name_plural = 'article_categories'


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    entry = models.TextField()

    # https://www.geeksforgeeks.org/datetimefield-django-models/
    # https://stackoverflow.com/questions/56310322/django-datetimefield-with-auto-now-add-asks-for-default
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:article-detail', args=[self.pk])

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'article'
        verbose_name_plural = 'articles'
