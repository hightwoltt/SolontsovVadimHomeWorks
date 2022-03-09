from logging import raiseExceptions
import random
from sys import exec_prefix
from tokenize import group
from typing import Any
from datetime import datetime
import names

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, CustomUser
from django.core.management.base import BaseCommand
from django.conf import settings

from proj.models import (
    Group,
    Account,
    Student,
    Professor,
)

class Command(BaseCommand):
    """Custom command for filling up database.
    """
    help = 'Custom command for filling up database.'

    def init(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_users(self) -> None:
        """Generate User objects."""

        TOTAL_USERS_COUNT = 500
        TOTAL_GROUPS_COUNT = 20
        TOTAL_PROFESSORS_COUNT = 10
        TOTAL_STUDENTS_COUNT = 500

        _email_patterns: tuple = (
            '@gmail.com', '@outlook.com', '@yahoo.com',
            '@inbox.ru', '@inbox.ua', '@inbox.kz',
            '@yandex.ru', '@yandex.ua', '@yandex.kz',
            '@mail.ru', '@mail.ua', '@mail.kz',
        )
        
        super_users: int = User.objects.filter(is_superuser="True")

        if super_users.count() <= 1:
            CustomUser.objects.create(
                is_superuser = True,
                is_staff = True,
                username = 'putin',
                email = 'vladimir_putin@mail.ru',
                password = 'КрымНаш228',
                first_name = 'Владимир',
                last_name = 'Путин',
            )
        elif super_users.count() >= 2:
            print('Superuser quantity is limited')

        # Строки 72 и 73 не соответствуют PEP-8 т.к 
        # после поереноса на новую строку в username 
        # и email подставляются лишние пробелы

        if CustomUser.objects.count() <= 1:
            try:
                inc: int
                for inc in range(TOTAL_USERS_COUNT):
                    user_password: str = 'Qwerty0123456789Qwerty'
                    user_first_name: str = names.get_first_name()
                    user_last_name: str = names.get_last_name()
                    CustomUser.objects.create(
                        first_name = user_first_name,
                        last_name = user_last_name,
                        password = make_password(user_password),
                        username = f'{user_first_name.lower()}_{user_last_name.lower()}',
                        email = f'{user_first_name.lower()}.{user_last_name.lower()}{random.choice(_email_patterns)}'),
            except Exception:
                print('Users count out of TOTAL_USERS_COUNT')            


        def generate_groups(self):

            if Group.objects.count() <= 1:
                try:
                    i: int
                    for i in range(TOTAL_GROUPS_COUNT):
                        Group.objects.create(
                            name = f'Группа{self.i}'
                        )
                except Exception:
                    print('Groups count out of TOTAL_GROUPS_COUNT')


        def generate_students(self):

            if Student.objects.count() <= 1:
                try:
                    s: int
                    user_stud = Student.objects.all()
                    for s in range(TOTAL_STUDENTS_COUNT):
                        Student.objects.create(
                            account = user_stud.pk(s)
                            age = random.radnint(15,27)
                            group =     
                            gpi = 

                        )
                except Exception:
                    print('Students count out of TOTAL_STUDENTS_COUNT')


        def generate_professors(self):

            TOPIC_CHOICES = (
                'Java',
                'Python',
                'Golang',
                'Typescript',
                'Swift',
                'PHP',
                'MatLab',
                'SQL',
                'Ruby',
                'Delphi'
                )
            
            if Professor.objects.count() <= 1:
                try:
                    j: int
                    group_num = 0
                    for j in range(TOTAL_PROFESSORS_COUNT):
                        professor_first_name: str = names.get_first_name()
                        professor_last_name: str = names.get_last_name()
                        Professor.objects.create(
                            full_name = f'{professor_first_name} {professor_last_name}',
                            topic = random.choise(TOPIC_CHOICES)
                            students = 
                        )
                except Exception:
                    print('Professors count out of TOTAL_PROFESSORS_COUNT')






    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()

        self._generate_users()

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )