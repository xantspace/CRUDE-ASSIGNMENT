from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        description = request.POST.get('description')
        if text:
            Todo.objects.create(title=text, description=description)
    return redirect('todo:todo_list')


def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo:todo_list')

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        new_text = request.POST.get('text')
        new_description = request.POST.get('description')
        if new_text:
            todo.title = new_text
            todo.description = new_description
            todo.save()
    return redirect('todo:todo_list')


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo:todo_list')