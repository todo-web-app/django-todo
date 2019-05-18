from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse

from .models import TodoList
from .forms import TodoLisForm


def index(request):
    form = TodoLisForm()
    todos = TodoList.objects.all()
    return render(request, 'todolist/index.html', {'todos': todos, 'form': form})


def add(request):
    if request.method == 'POST':
        form = TodoLisForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('todolist:index')
    else:
        form = TodoLisForm()
    return render(request, 'todolist/add.html', {'form': form})


def delete(request, todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todolist:index')


def done(request, todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    # toggle
    todo.done = not todo.done
    todo.save()
    return redirect('todolist:index')


def base_layout(request):
    form = TodoLisForm()
    return render(request, 'todolist/index.html', {'form': form})


def getdata(request):
    results = TodoList.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)
