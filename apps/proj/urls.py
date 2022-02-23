from django.urls import path
from . import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077

urlpatterns = [
    path('', views.index3),
    path('index2/', views.index2),
<<<<<<< HEAD
    path('admin/', views.admin),
    path('admin/show/', views.show),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
]
>>>>>>> 7bf75a6e7f46b3e8e32095e93b7f505a7e614077
