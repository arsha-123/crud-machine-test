from . import views
from django.urls import path

urlpatterns=[
    path('admin_login',views.admin_login,name='admin_login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('register',views.register,name='register'),
    path('active',views.active,name='active'),
]
    
