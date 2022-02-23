
from re import search
from tokenize import group
from typing import Optional
<<<<<<< HEAD
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
=======

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077
from . models import (Account, 
                    Student, 
                    Group,
                    Professor,
    )

class AccountAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

     # Задаюся поля в только для чтения
    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj:Optional[Account] = None
    ) -> tuple:

        # Readonly для описания
        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields


class StudentAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )
<<<<<<< HEAD
    # list_filter = (
    #     'gpa',
    #     'age',
    # )
    # search_fields = (
    #     'account__full_name',
    # )
    # list_display = (
    #     'age',
    #     'gpa',
    #     'group__name',
    #     'accuount__full_name',
    # )
    MAX_STUDENT_AGE = 16
    SUPER_STUDENT_NAME = 'ВладимирВладимировичПутин'
=======
   
    MAX_STUDENT_AGE = 16
    SUPER_STUDENT_NAME = 'DevAdmin'
>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077

    def student_age_validation(
        self,
        obj: Student
    ) -> tuple:
        if obj and obj.age <= self.MAX_STUDENT_AGE:
            return self.readonly_fields + ('age',)
        return self.readonly_fields
        
    # Задаюся поля в только для чтения
    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj:Optional[Student] = None
    ) -> tuple:

        result: tuple = self.student_age_validation(obj)
        return result

        # Readonly только если пользователю больше 16 лет
        if obj and obj.age > self.MAX_STUDENT_AGE:
            return self.readonly_fields + ('age',)
        return self.readonly_fields


class GroupAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
        )
    SPECIAL_NAME = 'supergroup'

    # Задаюся поля в только для чтения
    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj:Optional[Group] = None
    ) -> tuple:

        # Readonly только если прользователь в супергруппе
        if obj and obj.name == 'supergroup':
            return self.readonly_fields + ('name',)
        return self.readonly_fields


class ProfessorAdmin(admin.ModelAdmin):
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )
    pass

admin.site.register(
    Professor, ProfessorAdmin
)

admin.site.register(
    Group, GroupAdmin
)

admin.site.register(
    Student, StudentAdmin
)

admin.site.register(
    Account, AccountAdmin
)