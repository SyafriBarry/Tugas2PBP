from django.urls import path
from todolist.models import TodoList
from todolist.views import create_task, delete_task, register, show_todolist, switch_status
from todolist.views import login_user
from todolist.views import logout_user

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create-task'),
    path('switch_status/<int:pk>/', switch_status, name='switch_status'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
]