from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',                        views.index,    name='page_main'),
    path('show/<int:user_id>/',     views.show,     name='page_show'),
    path('delete/',                 views.delete,   name='page_delete'),
    path('register/',               views.register, name='page_register'),
    path('login/',                  views.login,    name='page_login'),
    path('logout/',                 views.logout,   name='page_logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 