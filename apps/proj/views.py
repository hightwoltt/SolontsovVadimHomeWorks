from cgitb import text
from multiprocessing import context
from os import name
from re import A
from tkinter import E
from urllib import response

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, QueryDict
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)
from auths.forms import CustomUserForm
from auths.models import CustomUser
from . models import (
    Homework,
    Student
) 

def index(request: WSGIRequest) -> HttpResponse:
    
    if not request.user.is_authenticated:
        return render(
            request,
            'proj/login.html'
        ) 

def index3(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = CustomUser.objects.all()
    context: dict = {
        'title': 'Главная страница',
        'users': users,
    }
    return render(
        request,
        'index.html',
        context
    )

def admin(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'admin.html',
        context = {"ctx_users":CustomUser.objects.all()},
    )

def show(request: WSGIRequest, user_id: str) -> HttpResponse:
    
    user: User = CustomUser.objects.get(id=user_id)
    context: dict = {
        'ctx_title': 'Профиль',
        'ctx_user': user,
    }
    return render(
        request,
        'show.html',
        context=context
    )

def delete(request: WSGIRequest, username: str) -> HttpResponse:
    
    user: User = CustomUser.objects.get(username=username)
    context: dict = {
        'ctx_title': 'Профиль',
        'ctx_user': user,
    }
    return render(
        request,
        'delete.html',
        context=context
    )

def register(request: WSGIRequest) -> HttpResponse:
    
    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    if form.is_valid():
        user: CustomUser = form.save(
            commit=False
        )
        email: str = form.cleaned_data['email']
        password: str = form.cleaned_data['password']
        user.email = email
        user.set_password(password)
        user.save()

        user: CustomUser = dj_authenticate(
            email=email,
            password=password
        )
        if user and user.is_active:

            dj_login(request, user)

            homeworks: QuerySet = Homework.objects.filter(
                user=request.user
            )
            return render (
                request,
                'proj/index.html',
                {'homeworks': homeworks}
            )
    context: dict = {
        'from': form
    }

    return render (
        request,
        'proj/register.html',
        context
    )
def login(request: WSGIRequest) -> HttpResponse:

    if request.method == 'POST':
        email: str = request.POST['email']
        password: str = request.POST['password']

        user: CustomUser = dj_authenticate(
            email=email,
            password=password
        )

        if not user:
            return render(
                request,
                'proj/login.html',
                {'error_message': 'Невереные данные'}
            )
        if not user.is_active:
            return render(
                request,
                'proj/login.html',
                {'error_message': 'Ваш аккаунт был удален'}
            )
        dj_login(request, user)

        homeworks: QuerySet = Homework.objects.filter(
            user=request.user
        )
        return render(
            request,
            'proj/index.html',
            {'homeworks': homeworks}
        )
    return render(
        request,
        'proj/login.html'
    )


def logout(request: WSGIRequest) -> HttpResponse:

    dj_logout(request)

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    context: dict = {
        'form': form,
    }
    return render(
        request,
        'proj/login.html',
        context
    )
