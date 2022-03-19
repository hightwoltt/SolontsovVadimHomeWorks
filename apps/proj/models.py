
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.db.models import QuerySet
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

from abstracts.models import AbstractDateTime
from auths.models import CustomUser


class StudentQuerySet(QuerySet): 
    ADAULT_AGE = 18 

    def get_adault_students(self)-> QuerySet:
        return self.filter(
            age__gte=self.ADAULT_AGE
        )


class AccountQuerySet(QuerySet):
    HIGH_GPA_LVL = 4.0

    def get_superusers(self)-> QuerySet:
        return self.filter(
            user__is_superuser=True
        )


class GroupQuerySet(QuerySet):
    HIGHT_GPA_LVL = 4.0

    def get_students_with_high_gpa(self) -> QuerySet:
        return self.filter(
            self.Stuent.gpa__gt == self.HIGHT_GPA_LVL
        )
    
# class HomeworkQuerySet(QuerySet):
    
#     def get_delete_homeworks(self) -> QuerySet:
#         if Homework.DateTimeDeleted == NULL:
#             return
#         else:
#             self.filter(
#                 self.Homework.not_deleted == False
#             )


class HomeworkQuerySet(QuerySet):
    
    def get_delete_fields(self) -> QuerySet:
        return  self.filter(
            self.Homework.not_deleted == True
        )

class FileQuerySet(QuerySet):
    
    def get_is_checked_homeworks(self) -> QuerySet:
        return self.filter(
            homework__is_checked=True
        )

class Group(AbstractDateTime):
    pass
    GROUP_NAME_MAX_LENGTH = 10

    name = models.CharField(
        max_length=GROUP_NAME_MAX_LENGTH
    )

    def __str__(self) -> str:
        return f'Group: {self.name}'

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Student(AbstractDateTime):

    GROUP_NAME_MAX_LENGHT = 15
    MAX_AGE = 27

    account = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    age = models.IntegerField(
        'Возраст студента'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT
    )
    gpi = models.FloatField(
        'Средний балл',

    )

    def __str__(self) -> str:
        return f'Аккаунт: {self.account} \
        Возраст {self.age} \
        Группа {self.group.name} \
        Cредний балл {self.gpi}'

    def save(
        self, 
        *args: tuple,
        **kwargs: dict
    ) -> None:
        if self.age > self.MAX_AGE:
            raise ValidationError(
                f'Максимально допустимый возраст {self.MAX_AGE}'
            )
        super().save(*args, **kwargs)

        
    objects = AccountQuerySet().as_manager()

    class Meta:
        ordering = (
            'group','age'
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Professor(AbstractDateTime):

    FULL_NAME_MAX_LENGTH = 40
    TOPIC_MAX_LENGTH = 30

    TOPIC_JAVA = 'java'
    TOPIC_PYTHON = 'python'
    TOPIC_GOLANG = 'golang'
    TOPIC_TYPESCRIPT = 'typescript'
    TOPIC_SWIFT = 'swift'
    TOPIC_PHP = 'php'
    TOPIC_MATLAB = 'matlab'
    TOPIC_SQL = 'sql'
    TOPIC_RUBY = 'ruby'
    TOPIC_DELPHI = 'delphi'

    TOPIC_CHOICES = (
        (TOPIC_JAVA,'Java'),
        (TOPIC_PYTHON,'Python'),
        (TOPIC_GOLANG,'Golang'),
        (TOPIC_TYPESCRIPT,'Typescript'),
        (TOPIC_SWIFT,'Swift'),
        (TOPIC_PHP,'PHP'),
        (TOPIC_MATLAB,'MatLab'),
        (TOPIC_SQL,'SQL'),
        (TOPIC_RUBY,'Ruby'),
        (TOPIC_DELPHI,'Delphi')
    )
    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=FULL_NAME_MAX_LENGTH
    )
    topic = models.CharField(
        verbose_name='Предмет',
        choices=TOPIC_CHOICES,
        default=TOPIC_JAVA,
        max_length=TOPIC_MAX_LENGTH
    )
    students = models.ManyToManyField(
        Student
    )

    def __str__(self) -> str:
        return f'Преподаватель: {self.full_name} \
        Предмет {self.topic} \
        Студенты {self.students}'

    def save(
        self,
        *args,
        **kwargs
        ):
        super().save(*args, **kwargs)

    class Meta:
        ordering = (
            'topic',
        )
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Homework(AbstractDateTime):
    user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT
    )
    title = models.CharField(max_length=100)

    subject = models.CharField(max_length=50)
    
    logo = models.ImageField(
        'Лого домашней работы',
        upload_to='homework/',
        max_length=255
    )
    is_checked = models.BooleanField(default=False)

    objects = HomeworkQuerySet().as_manager()

    def __str__(self) -> str:
        return f'{self.subject} | {self.title}'

    class Meta:
        ordering = (
            'datetime_created',
        )
        verbose_name = 'Домашняя работа'
        verbose_name_plural = 'Домашние работы'

class File(AbstractDateTime):

    homework = models.ForeignKey(
        Homework, on_delete=models.PROTECT
    )

    title = models.CharField(max_length=100)
    obj = models.FileField(
        'Объект файла',
        upload_to='homework_files/%Y/%m/%d/',
        max_length=255
    )

    objects = FileQuerySet().as_manager()

    def __str__(self) -> str:
        return f'{self.homework.title} | {self.title}'

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'