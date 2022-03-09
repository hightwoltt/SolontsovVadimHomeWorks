
from msilib.schema import File
from re import search
from tokenize import group
from typing import Optional
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from auths.models import CustomUser

from . models import (
                    File,
                    Homework,
                    Student, 
                    Group,
                    Professor,
    )


class StudentAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )
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
   
    MAX_STUDENT_AGE = 16
    SUPER_STUDENT_NAME = 'DevAdmin'

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


class HomeworkAdmin(admin.ModelAdmin):

    readonly_fields = (
        'student_name',
    )


class FileAdmin(admin.ModelAdmin):

    readonly_fields = (
        'file',
        'title'
    )
    

admin.site.register(
    File, FileAdmin
) 

admin.site.register(
    Homework, HomeworkAdmin
) 

admin.site.register(
    Professor, ProfessorAdmin
)

admin.site.register(
    Group, GroupAdmin
)

admin.site.register(
    Student, StudentAdmin
)
