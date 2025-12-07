from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # Add your app's URL patterns here
    path('', views.todo_list, name='todo_list'), # List all todos
    path('add/', views.add_todo, name='add_todo'),
    path('toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'), # Should show form
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    
]
