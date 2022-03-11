from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admin),
    path('index2/', views.index3),

    path(
        'show/<int:user_id>/',
        views.show,
        name='page_show'
    ),

    path('delete/',
    views.delete, 
    name='page_delete'
    ),

    path('register/',
    views.register,
    name='registration_form'
    ),

    path('login/',
    views.login,
    name='login_form'
    ),

    path('logout/',
    views.logout,
    name='logout_form'
    ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 