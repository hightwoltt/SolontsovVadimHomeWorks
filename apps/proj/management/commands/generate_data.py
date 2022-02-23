from logging import raiseExceptions
import random
from tokenize import group
from typing import Any
from datetime import datetime
import names

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
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
<<<<<<< HEAD
=======

>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077
    Test data only
    """
    help = 'Custom command for filling up database.'

    def init(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_users(self) -> None:
        """Generate User objects."""

<<<<<<< HEAD
        TOTAL_USERS_COUNT = 500
=======
        TOTAL_USERS_COUNT = 1000
>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077

        _email_patterns: tuple = (
            '@gmail.com', '@outlook.com', '@yahoo.com',
            '@inbox.ru', '@inbox.ua', '@inbox.kz',
            '@yandex.ru', '@yandex.ua', '@yandex.kz',
            '@mail.ru', '@mail.ua', '@mail.kz',
        )
        
        super_users: int = User.objects.filter(is_superuser="True")

        if super_users.count() <= 1:
            User.objects.create(
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

        if User.objects.count() <= 2:
            try:
                inc: int
                for inc in range(TOTAL_USERS_COUNT):
                    user_password: str = 'Qwerty0123456789Qwerty'
                    user_first_name: str = names.get_first_name()
                    user_last_name: str = names.get_last_name()
                    User.objects.create(
                        first_name = user_first_name,
                        last_name = user_last_name,
                        password = make_password(user_password),
                        username = f'{user_first_name.lower()}_{user_last_name.lower()}',
                        email = f'{user_first_name.lower()}.{user_last_name.lower()}{random.choice(_email_patterns)}'),
            except Exception:
                print('Users count out of TOTAL_USERS_COUNT')
<<<<<<< HEAD
            
=======

            

>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077
    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()

        self._generate_users()

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )