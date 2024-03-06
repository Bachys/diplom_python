from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('coctails/', views.coctails, name='coctails'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginuser, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logoutuser, name='logout'),
]

