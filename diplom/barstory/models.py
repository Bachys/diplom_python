from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фамилия пользователя')
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True, verbose_name='Псевдоним')
    bio = models.TextField(blank=True, null=True, verbose_name='О пользователе')
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/icon.jpg', verbose_name='Фото')
    workplace = models.CharField(max_length=200, blank=True, null=True, verbose_name='Место работы(ссылка)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистраци')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'
        ordering = ['-created']


class ClassicCocktails(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название коктейля')
    text = models.TextField(blank=True, verbose_name='История коктейля')
    photo = models.ImageField(upload_to='photos/image', default='default.jpg', verbose_name='Фото')
    recept = models.TextField(blank=True, verbose_name='Рецепт коктейля')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'коктейль'
        verbose_name_plural = 'коктейли'
        ordering = ['title']


class Slider(models.Model):
    img = models.ImageField(upload_to='slider_img/', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'слайд'
        verbose_name_plural = 'Слайды'
