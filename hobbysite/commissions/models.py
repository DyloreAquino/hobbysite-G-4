"""Models file."""
from django.db import models
from django.urls import reverse
from user_management.models import Profile
# Create your models here.

STATUS_CHOICES = (
    ("OPEN", "Open"),
    ("FULL", "Full"),
    ("COMPLETE", "Completed"),
    ("DISCONTINUED", "Discontinued")
)

class Commission(models.Model):
    """A model for commissions."""

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )
    requiredPeople = models.IntegerField()
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()

    class Meta():
        """Orders the commissions based on date created."""

        ordering = ['createdOn']

    def __str__(self):
        """Return the name of the object."""
        return self.title

    def get_absolute_url(self):
        """Return the url link of the object."""
        return reverse('commissions:commissions-detail', args=[self.pk])



