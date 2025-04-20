from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Todolist
from django.views.decorators.http import require_POST
from .forms import TodoListForm

def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context)


@require_POST
def addTodoItem(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')


def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')
