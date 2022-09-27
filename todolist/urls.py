from django.urls import path
from todolist.models import TodoList
from todolist.views import create_task, register, show_todolist
from todolist.views import login_user
from todolist.views import logout_user

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create-task'),
]