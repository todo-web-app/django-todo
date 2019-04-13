from django.shortcuts import render, redirect

from .models import TodoList
from .forms import TodoLisForm


def index(request):
    todos = TodoList.objects.all()
    return render(request, 'todolist/index.html', {'todos': todos})


def add(request):
    if request.method == 'POST':
        form = TodoLisForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('todolist:index')
    else:
        form = TodoLisForm()
    return render(request, 'todolist/add.html', {'form': form})


def edit(request, todo_id):
    todo = TodoList.objects.get(pk=todo_id)

    if request.method == 'POST':
        form = TodoLisForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            return redirect('todolist:index')
    else:
        form = TodoLisForm(instance=todo)
    return render(request, 'todolist/add.html', {'form': form}) 

