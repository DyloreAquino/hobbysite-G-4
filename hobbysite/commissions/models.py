"""Models file."""
from django.db import models
from django.urls import reverse
# Create your models here.


class Commission(models.Model):
    """A model for commissions."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    requiredPeople = models.IntegerField()
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()

    def __str__(self):
        """Return the name of the object."""
        return self.name

    def get_absolute_url(self):
        """Return the url link of the object."""
        return reverse('commissions:commissions-detail', args=[self.pk])


class Comment(models.Model):
    """A model for comments."""

    commission = models.ForeignKey(Commission,
                                   on_delete=models.CASCADE,
                                   related_name='commission')
    entry = models.TextField()
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()
