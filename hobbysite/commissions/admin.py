"""Admin file."""
from django.contrib import admin
from .models import Commission, Job, JobApplication
# Register your models here.


class JobAppInline(admin.TabularInline):
    """Admin access to JobApplication"""
    model = JobApplication
    list_display = [
        'applicant',
        'status',
    ]
    readonly_fields = ['applied_on']


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
    inlines = [JobAppInline]

    list_display = (
        'commission',
        'role',
        'manpower_required',
        'status'
    )


class TempJobAppAdmin(admin.ModelAdmin):
    """TO DELETE LATER"""

    model = JobApplication
    list_display = (
        'job',
        'applicant',
        'status',
    )

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, TempJobAppAdmin)
