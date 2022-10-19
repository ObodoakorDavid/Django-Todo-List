from django.shortcuts import render, redirect
from .models import Todo
from .forms import Todoform
# Create your views here.

def todo_list(request):
    todolist = Todo.objects.all()
    context = {
        'todolist': todolist
    }
    return render(request, 'todo/todo_list.html', context)


def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }

    return render(request, 'todo/todo_detail.html', context)

def todo_create(request):
    form = Todoform(request.POST)
    print(request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # print(name, due_date)
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        form.save()
        return redirect('/todo_created')
    context = {'form': form}

    return render(request, 'todo/todo_create.html', context)


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = Todoform(request.POST or None, instance=todo)
    if form.is_valid():
        # print(form.cleaned_data)
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # print(name, due_date)
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        form.save()
        return redirect('/todo_updated')
    context = {'form': form}

    return render(request, 'todo/todo_update.html', context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todo_deleted')

def todo_deleted(request):
    return render(request, 'todo/todo_deleted.html')

def todo_created(request):
    return render(request, 'todo/todo_created.html')

def todo_updated(request):
    return render(request, 'todo/todo_updated.html')

