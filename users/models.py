from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Расширенная модель пользователя, основанная на AbstractUser, с дополнительными полями для хранения
    персональной информации и интеграции с внешними системами.

    Поля:
        - username: исключен, так как используется email в качестве уникального идентификатора.
        - first_name (CharField): Имя пользователя, необязательное.
        - last_name (CharField): Фамилия пользователя, необязательное.
        - patronymic (CharField): Отчество пользователя, необязательное.
        - email (EmailField): Уникальный адрес электронной почты, используется как логин.
        - avatar (ImageField): Фото профиля пользователя, необязательное.
        - phone (CharField): Телефонный номер, необязательное.
        - city (CharField): Город проживания, необязательное.
        - country (CharField): Страна проживания, необязательное.
        - token (CharField): Токен для аутентификации или интеграции, необязательное.
        - tg_id (CharField): Идентификатор Telegram, необязательное.
        - created_at (DateTimeField): Дата и время создания записи, автоматически устанавливается.
        - updated_at (DateTimeField): Дата и время последнего обновления, автоматически обновляется.
        - is_active (BooleanField): Статус активности пользователя, по умолчанию — активен.

    Методы:
        - __str__: возвращает email пользователя для удобства отображения.

    Метаданные:
        - verbose_name: "Пользователь"
        - verbose_name_plural: "Пользователи"
    """
    username = None
    first_name = models.CharField(max_length=50, verbose_name="Имя", blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", blank=True, null=True)
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество")
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to="users/", blank=True, null=True, verbose_name="Фотография")
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="Телефон")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name="Страна")
    token = models.CharField(max_length=150, verbose_name="token", blank=True, null=True)
    tg_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Telegram ID")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, )
    is_active = models.BooleanField(blank=True, null=True, default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
