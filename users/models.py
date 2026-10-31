from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, verbose_name='Номер Телефона', blank=True, null=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна', blank=True, null=True, help_text='Введите страну проживания')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', blank=True, null=True, help_text='Загрузите свой аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Поьзователи'

    def __str__(self):
        return self.email
