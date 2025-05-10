"""Models file."""
from django.db import models
from django.urls import reverse
from user_management.models import Profile
# Create your models here.


class Commission(models.Model):
    """A model for commissions."""

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
    description = models.TextField()
    requiredPeople = models.IntegerField()
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()

    class Meta():
        """Orders the commissions based on date created."""

        ordering = ['-createdOn']

    def __str__(self):
        """Return the name of the object."""
        return self.title

    def get_absolute_url(self):
        """Return the url link of the object."""
        return reverse('commissions:commissions-detail', args=[self.pk])


class Comment(models.Model):
    """A model for comments."""

    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    entry = models.TextField()
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()

    class Meta():
        """Orders the comments based on date created."""

        ordering = ['-createdOn']
