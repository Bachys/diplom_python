from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User, Profile


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'username', 'bio', 'profile_image', 'workplace', 'town')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Ник',
            'bio': 'О себе',
            'profile_image': 'Аватар',
            'workplace': 'Место работы',
            'town': 'Город'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control1'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 20}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'workplace': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
        }
