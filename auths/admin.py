from datetime import datetime
from django.contrib import admin
from typing import Optional
from django.core.handlers.wsgi import WSGIRequest

from . models import (CustomUser)

class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ()

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj:Optional[CustomUser] = None
    ) -> tuple:

        if obj:
            return self.readonly_fields()
        else:
            return self.readonly_fields(
                'email',
                'datetime_joined',
                'is_staff',
                'is_root',
                 'last_name',
                 'first_name',
            )
        return self.readonly_fields

admin.site.register(
    CustomUser, CustomUserAdmin
)

