# Generated by Django 5.0.2 on 2024-03-05 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barstory', '0003_alter_classiccocktails_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя пользователя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия пользователя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='workplace',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Место работы(ссылка)'),
        ),
    ]