from django.shortcuts import render
from .models import TodoList


def index(request):
    todos = TodoList.objects.all()
    return render(request, 'todolist/index.html', {'todos': todos})
