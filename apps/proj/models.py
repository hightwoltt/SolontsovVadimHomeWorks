<<<<<<< HEAD


from venv import create
from django.db import models

=======
from venv import create

from django.db import models
>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.db.models import QuerySet

from abstracts.models import AbstractDateTime


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
    

class Account(AbstractDateTime):

    ACCOUNT_FULL_NAME_MAX_LENGTH = 30
    GROUP_NAME_MAX_LENGHT = 15

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=ACCOUNT_FULL_NAME_MAX_LENGTH
    )
    description = models.TextField()
    
    def __str__(self) -> str:
        return f'Account:{self.user.id} / {self.full_name}'

    class Meta:
        ordering = (
            'full_name',
        )
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    objects = AccountQuerySet().as_manager()


class Group(AbstractDateTime):

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

<<<<<<< HEAD

class Foo():
    pass


=======
>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077
class Student(AbstractDateTime):

    GROUP_NAME_MAX_LENGHT = 15
    MAX_AGE = 27

    account = models.ForeignKey(
        Account,
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