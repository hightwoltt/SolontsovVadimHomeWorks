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

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','is_active',)
    list_filter = ('email', 'is_active',)
    fieldsets = (
        (
            None, {
                'fields': (
                    'email', 'password',
                ),
            }
        ),
        (
            'Permissions', {
                'fields': ('is_active',)
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email', 'password1', 'password2', 'is_active',
                ),
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    # readonly_fields = ()

    # def get_readonly_fields(
    #     self,
    #     request: WSGIRequest,
    #     obj:Optional[CustomUser] = None
    # ) -> tuple:

    #     if obj:
    #         return self.readonly_fields()
    #     else:
    #         return self.readonly_fields(
    #             'email',
    #             'datetime_joined',
    #             'is_staff',
    #             'is_root',
    #             'last_name',
    #             'first_name',
    #         )
    #     return self.readonly_fields

admin.site.register(
    CustomUser, CustomUserAdmin
)

