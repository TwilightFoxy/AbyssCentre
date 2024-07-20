from django.contrib import admin
from django.urls import path, include
from .views import home, login_success, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('AuthApp.urls', namespace='authapp')),
    path('home/', home, name='home'),
    path('login-success/', login_success, name='login_success'),
    path('dashboard/', dashboard, name='dashboard'),
    path('queue/', include('QueueApp.urls')),  # Добавлены URL-ы для QueueApp
    path('', home, name='home'),
]
