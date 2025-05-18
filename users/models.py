from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name="name", help_text="Имя", )
    last_name = models.CharField(max_length=50, verbose_name="surname", help_text="Фамилия", )
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name="patronymic",
                                  help_text="Отчество (если есть)", )
    email = models.EmailField(unique=True, verbose_name="email", help_text="Электронная почта", )
    avatar = models.ImageField(upload_to="users/", blank=True, null=True, verbose_name="avatar",
                               help_text="Фотография", )
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="phone", help_text="Номер телефона", )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="city", help_text="Город", )
    country = models.CharField(max_length=255, blank=True, null=True,
                               verbose_name="country", help_text="Гражданство", )
    token = models.CharField(max_length=150, verbose_name="token", blank=True, null=True)
    tg_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Telegram ID")
    created_at = models.DateTimeField(default=timezone.now, help_text="Дата регистрации")
    updated_at = models.DateTimeField(auto_now=True, help_text="Дата изменения")
    is_active = models.BooleanField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
