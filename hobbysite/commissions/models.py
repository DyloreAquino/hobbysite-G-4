"""Models file."""
from django.db import models
from django.urls import reverse
from user_management.models import Profile
# Create your models here.

DEFAULT_STATUS_CHOICES = (
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
        null=True
    )
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=DEFAULT_STATUS_CHOICES,
        default='OPEN'
    )
    requiredPeople = models.IntegerField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now_add=True)

    class Meta():
        """Orders the commissions based on date created."""

        ordering = ['createdOn']

    def __str__(self):
        """Return the name of the object."""
        return self.title

    def get_absolute_url(self):
        """Return the url link of the object."""
        return reverse('commissions:commissions-detail', args=[self.pk])


class Job(models.Model):
    """A model for Jobs on each Commission"""

    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        null=True
    )
    role = models.CharField(max_length=255, null=True)
    manpower_required = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=DEFAULT_STATUS_CHOICES[:2],
        default='OPEN'
    )

    class Meta:
        """Meta of the Job model to order by status & manpower"""
        # Status needs to be put in descending since 
        # we're expecting Open before Full and it sorts alphabetically
        ordering = ["-status", "-manpower_required", "role"]
