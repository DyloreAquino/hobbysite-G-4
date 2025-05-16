from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    """Profile inline for user admin"""

    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    """User admin for user model"""

    inlines = [ProfileInline,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
