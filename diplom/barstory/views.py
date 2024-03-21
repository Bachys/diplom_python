from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ClassicCocktails


def single_coctail(request):
    coc = ClassicCocktails.objects.all()
    return render(request, 'barstory/singlcoctail.html', {'coc': coc})


def news(request):
    return render(request, 'barstory/news.html')


def home_page(request):
    return render(request, 'barstory/index.html')


def coctails(request):
    coc = ClassicCocktails.objects.all()
    return render(request, 'barstory/coctails.html', {'coc': coc})


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
            return redirect('profile')


def registration(request):
    if request.method == 'GET':
        return render(request, 'barstory/registration.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                return render(request, 'barstory/registration.html', {'form': UserCreationForm,
                                                                      'error': "Пользователь с таким именем уже существует"})
        else:
            return render(request, 'barstory/registration.html', {'form': UserCreationForm,
                                                                  'error': "Пароли не совпадают"})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home_page')
