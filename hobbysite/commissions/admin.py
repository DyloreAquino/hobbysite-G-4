"""Admin file."""
from django.contrib import admin
from .models import Commission
# Register your models here.


class CommissionAdmin(admin.ModelAdmin):
    """Admin access to commissions."""

    model = Commission


admin.site.register(Commission, CommissionAdmin)
