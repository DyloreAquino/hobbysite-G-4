"""Admin file."""
from django.contrib import admin
from .models import Commission, Job
# Register your models here.


class CommissionAdmin(admin.ModelAdmin):
    """Admin access to commissions."""

    model = Commission


class JobAdmin(admin.ModelAdmin):
    """Admin access to Job"""

    model = Job

    list_display = (
        'commission',
        'role',
        'manpower_required',
        'status'
    )

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
