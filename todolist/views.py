from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse

from .models import TodoList
from .forms import TodoLisForm


def index(request):
    """Top page."""
    form = TodoLisForm()
    todos = TodoList.objects.all()
    return render(request, 'todolist/index.html', {'todos': todos, 'form': form})


def add(request):
    """Add a todo with a form."""
    if request.method == 'POST':
        form = TodoLisForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('todolist:index')
    else:
        form = TodoLisForm()
    return render(request, 'todolist/add.html', {'form': form})


def delete(request, todo_id):
    """Delete a todo."""
    todo = TodoList.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todolist:index')


def done(request, todo_id):
    """Mark the task as done."""
    todo = TodoList.objects.get(pk=todo_id)
    # toggle
    todo.done = not todo.done
    todo.save()
    return redirect('todolist:index')


def base_layout(request):
    """Duplicate with index???"""
    form = TodoLisForm()
    return render(request, 'todolist/index.html', {'form': form})


def get_data(request):
    """Json list of result."""
    results = TodoList.objects.all()
    jsondata = serializers.serialize('json',results)
    return HttpResponse(jsondata)
