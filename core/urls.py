from django.urls import path, include
from . import views
app_name = 'core'


urlpatterns = [
    path('', views.HomeView, name='home'),

    path('todo/', views.ToDoList, name='todo'),
    path('todo/edit/<int:id>/', views.ToDoEdit, name='todo_edit'),
    path('todo/mark_completed/<int:id>/', views.ToDoMarkComplete, name='todo_mark_completed'),
    path('todo/mark_deleted/<int:id>/', views.ToDoMarkDelete, name='todo_mark_deleted'),
    path('todo/mark_important/<int:id>', views.ToDoMarkImportant, name='todo_mark_important'),
    path('todo/permanent_delete/<int:id>', views.ToDoPermanentDelete, name='todo_permanent_delete'),
    path('todo/revive_task/<int:id>', views.ToDoReviveTask, name='todo_revive_task'),

    path('notes/', views.NotesList, name='notes'),

]
