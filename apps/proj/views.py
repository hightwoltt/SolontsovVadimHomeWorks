
from typing import Optional

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
from django.template import loader
from django.views import View

from auths.forms import CustomUserForm
from auths.models import CustomUser
from abstracts.hanlers import ViewHandler
from . models import (
    Homework,
    Student
)

class IndexView(ViewHandler, View):

    template_name = 'proj/index.html'

    queryset: QuerySet = Homework.objects.filter()
    
    def get(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ):

        response: Optional[HttpResponse] = self.get_validated_response(
            request
        )
        if response: 
            return response

        homeworks: QuerySet = Homework.objects.filter(
            user=request.user
        )
        if not homeworks:
            homeworks = self.queryset

        context: dict = {
            'ctx_title': 'Главная',
            'ctx_homeworks': homeworks,
        }
           
        return self.get_http_response(
            request,
            self.template_name,
            context,
        )

class RegisterView(ViewHandler, View):

    template_name = 'proj/register.html'
    queryset: QuerySet = Homework.objects.filter()
    
    def get(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ):
        
        form: CustomUserForm = CustomUserForm(
            request.POST,
        )

        homeworks: QuerySet = Homework.objects.filter(
            user=request.user
        )
        context: dict = {
            'form': form,
        }
        template_name = loader.get_template(
            'proj/register.html',
        )

        return HttpResponse(
            template_name.render(
                context,
                request,
            ),
            content_type = 'text/html',
        )

    def post(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ):

        form: CustomUserForm = CustomUserForm(
            request.POST,
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
                template_name = loader.get_template(
                    'proj/page_main.html'
                )
                return HttpResponse(
                    template_name.render(
                    context, request
                    ),
                    content_type='text/html'
                    )

        context: dict = {
            'form': form,
        }

        return self.get_http_response(
            request,
            self.template_name,
            context,
        )


class LoginView(ViewHandler, View):

    template_name = 'proj/login.html'

    queryset: QuerySet = Homework.objects.get_not_deleted()

    def get(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ):

        form: CustomUserForm = (
            request.POST
        )

        homework: QuerySet = Homework.objects.filter(
            user=request.user
        )
        
        context: dict = {
            'form': form,
        }

        template_name: str = 'proj/login.html'

        return self.get_http_response(
            request,
            template_name,
            context, 
        )

    def post(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs
    ):

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

        context: dict = {
            'homeworks': homeworks
        }

        return self.get_http_response(
            request,
            self.template_name,
            context,
        )

def Index3View(ViewHandler, View):

    template_name = 'proj/index.html'

    def get(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs
    ):

        users: QuerySet = CustomUser.objects.all()

        context: dict = {
            'title': 'Главная страница',
            'users': users,
        }
        return self.get_http_response(
            request,
            self.template_name,
            context,
        )


class AdminView(ViewHandler, View):

    template_name = 'proj/admin.html'

    def get(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs
    ):

        context: dict = {
            "ctx_users":CustomUser.objects.all()
            }

        template_name = 'proj/admin.html'
     
        return self.get_http_response(
            request,
            self.template_name,
            context,
        )


class ShowView(ViewHandler, View):
    
    queryset: QuerySet = Homework.objects.get_not_deleted()
    
    template_name = 'proj/show.html'

    def get(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ):
        homework_id: int = kwargs.get('homework_id', 0)
        # user: User = CustomUser.objects.get(id=user_id)

        homework: Optional[Homework] = None
        
        try:
            homework = self.queryset.filter(user=self.request.user)\
                .get(id=homework_id)
            
        except Homework.DoesNotExist:
            return self.get_http_response(
                request,
                'proj/login.html'
            )
        else:
            context: dict = {
                'ctx_title': 'Домашние задания',
                'ctx_homework': homework,
            }
        
            return self.get_http_response(
                request,
                self.template_name,
                context,
            )


class  LogoutView(ViewHandler, View):

    def get(
        self, 
        request: WSGIRequest,
        *args: tuple,
        **kwargs
    ):
        dj_logout(request)

        form: CustomUserForm = CustomUserForm(
            request.POST
        )

        context: dict = {
            'form': form,
        }

        template_name = 'proj/login.html'

        return self.get_http_response(
            request,
            template_name,
            context
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