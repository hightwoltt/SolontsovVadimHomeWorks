from cgitb import text
from multiprocessing import context
from os import name
from re import A
from urllib import response

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, QueryDict
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.shortcuts import render

from auths.models import CustomUser
from . models import (
                    Student) 

def index(request: WSGIRequest) -> HttpResponse:
    ''' Show last user '''

    student: Student = Student.objects.last()
    customuser: CustomUser
    login: CustomUser.email
    # account: Account = student.account
    # user: User = account.user
    
    # text: str = f'<h1>Имя пользователя - {CustomUser.is_active}<br>  \
    #     Имя аккаунта - {account.full_name} <br> \
    #     Средний балл - {student.gpi}<br> \
    #     </h1>'
    text: str = f'login {login}'
    response: HttpResponse = HttpResponse(text)
    return response

def index2 (request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Стартовая страница</h1>'
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