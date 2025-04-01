"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from . import models


class UserAdmin(BaseUserAdmin):
    """Define the admin page for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}), # noqa
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']


# UserAdmin is optional ---> admin.site.register(models.User)
admin.site.register(models.User, UserAdmin)
