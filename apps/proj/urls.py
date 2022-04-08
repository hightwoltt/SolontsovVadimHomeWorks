from django.urls import path, re_path

from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import(
    CreateHomeworkViev,
    IndexView,
    RegisterView,
    ShowView,
    LogoutView, 
    LoginView
)

urlpatterns = [
    path('',                        IndexView.as_view(),            name='page_main'),
    path('show/<int:homework_id>/', ShowView.as_view(),             name='page_show'),
    path('delete/',                 views.delete,                   name='page_delete'),
    path('register/',               RegisterView.as_view(),         name='page_register'),
    path('login/',                  LoginView.as_view(),            name='page_login'),
    path('logout/',                 LogoutView.as_view(),           name='page_logout'),
    path('create_hw/',              CreateHomeworkViev.as_view(),   name='page_create_hw'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 