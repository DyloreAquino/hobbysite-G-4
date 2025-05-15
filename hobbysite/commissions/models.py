"""Models file."""
from django.db import models
from django.urls import reverse
from user_management.models import Profile
from django.utils.translation import gettext_lazy as _


class Commission(models.Model):
    """
    A model for commissions.
    """
    COMM_STATUS_CHOICES = {
        "OPEN": "Open",
        "FULL": "Full",
        "COMPLETE": "Completed",
        "DISCONTINUED": "Discontinued"
    }
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=COMM_STATUS_CHOICES,
        default='OPEN'
    )
    required_people = models.IntegerField()
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created On"
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated On"
    )

    class Meta():
        """
        Orders the commissions based on date created.
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Return the name of the object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Return the url link of the object.
        """
        return reverse('commissions:commissions-detail', args=[self.pk])

    def is_commission_full(self):
        """
        Method to update the status of the commission
        when all jobs' statuses are full.

        It has a counter equal to the number of jobs
        and ticks down for each full job
        """
        filled_job_countdown = len(self.job.all())
        for job_instance in self.job.all():
            if job_instance.status == 'FULL':
                filled_job_countdown -= 1

        if filled_job_countdown == 0:
            return True
        else:
            return False


class Job(models.Model):
    """
    A model for Jobs on each Commission
    """
    JOB_STATUS_CHOICES = {
        "OPEN": "Open",
        "FULL": "Full"
    }
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        null=True,
        related_name='job'
    )
    role = models.CharField(max_length=255, null=True)
    manpower_required = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=JOB_STATUS_CHOICES,
        default='OPEN'
    )

    class Meta:
        """
        Meta of the Job model to order by status & manpower
        """
        # Status needs to be put in descending since
        # we're expecting Open before Full and it sorts alphabetically
        ordering = ["-status", "-manpower_required", "role"]

    def __str__(self):
        """
        Sets the name of the job to be human readable
        """
        return f"{self.commission.title} {self.role}"

    def get_open_slots_count(self):
        """
        Function to get the remaining number of open slots.
        (i.e. Difference between max manpower required and
        number of accepted job applications)
        Built-in to the Job for easier access.
        """
        slots_filled = len(self.job_application.all().filter(status="2"))
        return self.manpower_required - slots_filled


class JobApplication(models.Model):
    """
    Model for JobApplication
    """
    class JobAppStatus(models.TextChoices):
        """
        Subclass to set status of text choices
        that allows the status choices to be sorted

        Enum from
        https://docs.djangoproject.com/en/5.2/ref/models/fields/
        """
        PENDING = "1", _("Pending"),
        ACCEPTED = "2", _("Accepted"),
        REJECTED = "3", _("Rejected")

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        null=True,
        related_name='job_application'
    )
    applicant = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=JobAppStatus,
        default=JobAppStatus.PENDING
    )
    applied_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Applied On"
    )

    class Meta:
        """
        Sets ordering of JobApplication Model
        """
        ordering = ["status", "-applied_on"]
