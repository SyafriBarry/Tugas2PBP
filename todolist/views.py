from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from todolist.models import TodoList
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = TodoList.objects.filter(user=request.user)
    context = {
    'list_todo': data_todolist,
    'nama': request.user.username,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    context = {}
    if request.method == "POST":
        temp = TodoList(user=request.user, title=request.POST.get('todo'), description=request.POST.get('description'))
        temp.save()
        return redirect('todolist:show_todolist')
    return render(request, "create-task.html", context)

def switch_status(request, pk):
    temp = TodoList.objects.get(id=pk)
    if (temp.is_finished == False):
        temp.is_finished = True
    else:
        temp.is_finished = False
    temp.save()
    return redirect('todolist:show_todolist')

def delete_task(request, pk):
    temp = TodoList.objects.filter(pk=pk)
    temp.delete()
    return redirect('todolist:show_todolist')

