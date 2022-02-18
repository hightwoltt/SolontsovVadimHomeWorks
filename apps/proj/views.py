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

from . models import (Account, 
                    Student) 

def index(request: WSGIRequest) -> HttpResponse:
    ''' Show last user '''

    student: Student = Student.objects.last()
    account: Account = student.account
    user: User = account.user
    
    text: str = f'<h1>Имя пользователя - {user.first_name}<br>  \
        Имя аккаунта - {account.full_name} <br> \
        Средний балл - {student.gpi}<br> \
        </h1>'
    response: HttpResponse = HttpResponse(text)
    return response

def index2 (request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Стартовая страница</h1>'
    )

def index3(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = User.objects.all()
    context: dict = {
        'title': 'Главная страница',
        'users': users,
    }
    return render(
        request,
        'index.html',
        context
    )