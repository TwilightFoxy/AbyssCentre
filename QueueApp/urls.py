from django.urls import path
from . import views

urlpatterns = [
    path('', views.queue_list, name='queue_list'),
    path('add/', views.add_to_queue, name='add_to_queue'),
    path('update/<int:item_id>/<str:status>/', views.update_status, name='update_status'),
]
