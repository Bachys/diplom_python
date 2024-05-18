from django.urls import path
from . import views
from .views import ProfileUpdateForm

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('coctails/', views.coctails, name='coctails'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginuser, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logoutuser, name='logout'),
    path('single-new/<str:pk>/', views.single_new, name='single-new'),
    path('single/<str:pk>/', views.single_coctail, name='single'),
    path('politica/', views.politica, name='politica'),
    path('edit-prof/', views.edit_profile, name='edit-prof'),
    path('history/', views.history, name='history'),
    path('single-story/<str:pk>/', views.single_story, name='single-story'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('bartenders/', views.bartenders, name='bartenders'),
]
