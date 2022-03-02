import email
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin)
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    
    def create_user(
        self,
        email:str,
        password:str,
        **kwargs: dict
        ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')

        email = self.normalize_email(email)
        user: CustomUser = self.model(
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        kwargs: dict
    ) -> 'CustomUser':

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_root', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if kwargs.get('is_root') is not True:
            raise ValueError('Superuser must have is_root=True')

        user: 'CustomUser' = self.create_user(
            email,
            password,
            kwargs
        )
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта/Логин', unique=True)
    is_stuff = models.BooleanField(default=False)
    is_root = models.BooleanField(default=False)
    datetime_join = models.DateTimeField(
        verbose_name='Время регистрации', auto_now_add=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f'CustomUser: {self.email}'

    class Meta:
        ordering = (
            'email',
            'is_staff',
        )
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    def save(
        self, 
        *args: tuple,
        **kwargs: dict
    ) -> None:

        if self.email != self.email.lower():
            raise ValidationError(
                f'Email {self.email} is not lowercase'
            )
        super().save(*args, **kwargs)
