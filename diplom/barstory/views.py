from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from .models import ClassicCocktails, Profile, History, News, Events
from .forms import ProfileUpdateForm


def bartenders(request):
    search = ''

    if request.GET.get('search_query'):
        search = request.GET.get('search_query')

    barman = Profile.objects.filter(first_name__icontains=search)
    context = {
        'barman': barman,
        'title': "Бармены"

    }

    paginator = Paginator(barman, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'barman': page_obj})

    return render(request, 'barstory/bartenders.html', context)


def events(request):
    event = Events.objects.all()
    context = {
        'event': event,
        'title': 'Мероприятия',
    }
    return render(request, 'barstory/events.html', context)


def single_new(request, pk):
    obj = News.objects.get(id=pk)
    context = {'news': obj,
               'title': 'Что-то интересное',
               }
    return render(request, 'barstory/singlnew.html', context)


def contact(request):
    context = {'title': 'Контакты'}
    return render(request, 'barstory/contakts.html', context)


def single_story(request, pk):
    obj = History.objects.get(id=pk)
    context = {'story': obj,
               'title': 'История',
               }
    return render(request, 'barstory/singlhistory.html', context)


def history(request):
    story = History.objects.all()
    context = {
        'story': story,
        'title': 'Историческая справка',
    }

    paginator = Paginator(story, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'story': page_obj})

    return render(request, 'barstory/history.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            print('hello1')
            return redirect('profile')
        else:
            print('hello')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form': form,
        'title': 'Редактирование профиля',
    }
    return render(request, 'barstory/edit_profile.html', context)


def politica(request):
    context = {'title': 'Политика конфеденциальности'}
    return render(request, 'barstory/politica.html', context)


def single_coctail(request, pk):
    obj = ClassicCocktails.objects.get(id=pk)
    context = {'coctail': obj,
               'title': 'Страница коктейля'
               }
    return render(request, 'barstory/singlcoctail.html', context)


def home_page(request):
    news = News.objects.all()
    context = {'title': 'Новости',
               'news': news,
               }

    paginator = Paginator(news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'news': page_obj})

    return render(request, 'barstory/index.html', context)


def coctails(request):
    search = ''

    if request.GET.get('search_query'):
        search = request.GET.get('search_query')

    coc = ClassicCocktails.objects.filter(title__icontains=search)
    context = {
        'coc': coc,
        'title': 'Коктейли',
    }

    paginator = Paginator(coc, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'coc': page_obj, 'search': search})

    return render(request, 'barstory/coctails.html', context)


def profile(request):
    prof = Profile.objects.all()

    context = {'profile': prof,
               'title': 'Профиль'}
    return render(request, 'barstory/profile.html', context)


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'barstory/login.html',
                      {'form': AuthenticationForm(), 'title': 'Вход'})
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
        return render(request, 'barstory/registration.html',
                      {'form': UserCreationForm, 'title': 'Регистрация'})
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
