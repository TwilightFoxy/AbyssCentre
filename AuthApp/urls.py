# AuthApp/urls.py

from django.urls import path
from . import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    path('login-success/', views.login_success, name='login-success'),
]
