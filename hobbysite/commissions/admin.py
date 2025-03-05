"""Admin file."""
from django.contrib import admin
from .models import Commission, Comment
# Register your models here.


class CommissionAdmin(admin.ModelAdmin):
    """Admin access to commissions."""

    model = Commission


class CommentAdmin(admin.ModelAdmin):
    """Admin access to comment."""

    model = Comment


admin.site.register(Commission, CommissionAdmin)

admin.site.register(Comment, CommentAdmin)
