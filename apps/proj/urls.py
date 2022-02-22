from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index3),
    path('index2/', views.index2),
    path('admin/', views.admin),
    path('admin/show/', views.show),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)