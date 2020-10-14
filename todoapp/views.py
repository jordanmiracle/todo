from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TodoForm

def home(request):
    return render(request, 'todoapp/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todoapp/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodo')
            except IntegrityError:
                return render(request, 'todoapp/signupuser.html', {'form': UserCreationForm(), 'error': 'That user name has already been taken. Please choose a different name.'})
        else:
            return render(request, 'todoapp/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match.'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todoapp/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todoapp/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currenttodo')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todoapp/createtodo.html', {'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todoapp/createtodo.html', {'form':TodoForm(), 'error':'Bad data passed in. Try again.' })


def currenttodo(request):
    return render(request, 'todoapp/current.html')
