from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('edit/<int:id>', views.edit_task, name = 'edit'),
    path('update/<int:id>', views.update_task, name ='update'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle'),
]