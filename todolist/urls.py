from django.urls import path
from . import views


app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:todo_id>', views.edit, name='edit'),
]