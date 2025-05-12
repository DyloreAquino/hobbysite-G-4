"""Admin file."""
from django.contrib import admin
from .models import Commission, Job, JobApplication
# Register your models here.


class CommissionAdmin(admin.ModelAdmin):
    """Admin access to commissions."""

    model = Commission

    list_display = (
        'title',
        'status',
        'required_people',
        'created_on',
        'updated_on'
    )


class JobAdmin(admin.ModelAdmin):
    """Admin access to Job"""

    model = Job

    list_display = (
        'commission',
        'role',
        'manpower_required',
        'status'
    )


class JobAppAdmin(admin.ModelAdmin):
    """Admin access to JobApplication"""

    model = JobApplication

    list_display = (
        'job',
        'status',
        'applied_on'
    )

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobAppAdmin)
