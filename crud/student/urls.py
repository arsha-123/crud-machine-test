from django.urls import path
from . import views

urlpatterns = [
    path('student_login',views.student_login,name='student_login'),
    path('update',views.update,name='update'),
]
