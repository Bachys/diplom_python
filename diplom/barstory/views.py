from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home_page(request):
    return render(request, 'barstory/index.html')


def coctails(request):
    return render(request, 'barstory/coctails.html')


def profile(request):
    return render(request, 'barstory/profile.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'barstory/login.html',
                      {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'barstory/login.html',
                          {'form': AuthenticationForm(), 'error': "Неверны логин или пароль"})
        else:
            login(request, user)
            return redirect('currentuser')
