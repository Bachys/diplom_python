from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
