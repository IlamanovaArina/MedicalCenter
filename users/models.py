from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name="Имя",  blank=True, null=True,)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия",  blank=True, null=True,)
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество")
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to="users/", blank=True, null=True, verbose_name="Фотография")
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="Телефон")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name="Страна")
    token = models.CharField(max_length=150, verbose_name="token", blank=True, null=True)
    tg_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Telegram ID")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True,)
    is_active = models.BooleanField(blank=True, null=True, default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
