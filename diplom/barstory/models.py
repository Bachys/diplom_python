from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Events(models.Model):
    title = models.CharField(max_length=255, verbose_name='Мероприятие')
    event_photo = models.ImageField(upload_to='event_photos/image', default='events.jpg', verbose_name='Фото')
    event_text = models.TextField(blank=True, verbose_name='Мероприятие')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-created_at']


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок новости')
    new_photo = models.ImageField(upload_to='news_photos/image', default='news.jpg', verbose_name='Фото')
    news_text = models.TextField(blank=True, verbose_name='Новость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class History(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    history_photo = models.ImageField(upload_to='history_photos/image', default='history.jpg', verbose_name='Фото')
    short_text = models.TextField(verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Историяеская справка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'историю'
        verbose_name_plural = 'Исторические справки'
        ordering = ['-created_at']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фамилия пользователя')
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True, verbose_name='Псевдоним')
    bio = models.TextField(blank=True, null=True, verbose_name='О пользователе')
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/icon.jpg', verbose_name='Фото')
    workplace = models.CharField(max_length=200, blank=True, null=True, verbose_name='Место работы')
    town = models.CharField(max_length=200, blank=True, null=True, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистраци')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Профили'
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
        verbose_name_plural = 'Коктейли'
        ordering = ['title']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email, first_name=instance.first_name,
                               last_name=instance.last_name)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
