from csv import list_dialects
from datetime import datetime
from django.contrib import admin
from typing import Optional
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.admin import UserAdmin

from auths.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
from . models import (CustomUser)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = (
        ('Information', {
            'fields': (
                'email',
                'password',
                'date_joined',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_staff',
                'is_active',
            )
        }),
    )
    # NOTE: Used to define the fields that
    #       will be displayed on the create-user page
    #
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_active',
            ),
        }),
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'date_joined',
        'is_superuser',
        'is_staff',
        'is_active',
    )
    list_display = (
        'email',
        'password',
        'date_joined',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'email',
        'is_superuser',
        'is_staff',
        'is_active',
    )
    ordering = (
        'email',
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[CustomUser] = None
    ) -> tuple:
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'email',
        )

admin.site.register(
    CustomUser, CustomUserAdmin
)

