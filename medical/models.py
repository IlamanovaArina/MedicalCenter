from django.utils import timezone

from django.db import models

from config import settings


# Направление в медицине
class MedicalDirection(models.Model):
    name = models.CharField(max_length=100, verbose_name="Направление")
    description = models.CharField(max_length=500, verbose_name="Описание направления")

    class Meta:
        verbose_name = 'Направление в медицине'
        verbose_name_plural = 'Направления в медицине'

    def __str__(self):
        return self.name


# Доктора
class Doctors(models.Model):
    """
    Модель для хранения информации о врачах.

    Attributes:
        first_name (str): Имя врача.
        last_name (str): Фамилия врача.
        specialization (str): Специальность врача.
        experience (str): Стаж работы врача.
    """

    first_name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", null=True, blank=True)
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество")
    medical_direction = models.ForeignKey(MedicalDirection, on_delete=models.SET_NULL, null=True, blank=True)
    avatar = models.ImageField(upload_to="medical/", blank=True, null=True, verbose_name="Фотография")
    specialization = models.CharField(max_length=255, verbose_name="Специальность", null=True, blank=True)
    experience = models.CharField(max_length=255, verbose_name="Стаж работы", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь создавший этот экземпляр модели')

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'


# Услуги
class Services(models.Model):
    """
    Модель для хранения информации о медицинских услугах.
    """

    name = models.CharField(max_length=500, verbose_name="Название услуги")
    medical_direction = models.ForeignKey(MedicalDirection, related_name='services', on_delete=models.CASCADE)
    description = models.CharField(max_length=500, verbose_name="Описание услуги")
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь создавший этот экземпляр модели')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


# Отзывы
class Reviews(models.Model):
    """
    Модель для хранения отзывов о врачах.

    Attributes:
        DOCTOR_RATE (list[tuple[str, str]]): Список возможных оценок и их описаний.
        text (str): Текст отзыва, может быть пустым.
        rate (str): Оценка врача в виде звезд, выбирается из DOCTOR_RATE.
        user (ForeignKey): Пользователь, оставивший отзыв.
    """

    DOCTOR_RATE: list[tuple[str, str]] = [
        ("5", "Все отлично!"),
        ("4", "Все хорошо."),
        ("3", "Есть замечания"),
        ("2", "Не устроило"),
        ("1", "Категорически не устроило"),
    ]

    text = models.TextField(max_length=500, verbose_name="Отзыв", blank=True, null=True)
    rate = models.CharField(
        verbose_name="Количество звезд", max_length=100, choices=DOCTOR_RATE
    )
    doctors = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Доктор")
    services = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Услуга")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь, оставивший отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


# Информация
class Information(models.Model):
    """
    Модель для хранения контактной информации клиники.

    Attributes:
        phone (str): Номер телефона клиники.
        address (str): Адрес клиники.
    """
    text_from_the_main_page = models.CharField(max_length=500, null=True, blank=True,
                                               verbose_name="Информация с главной страницы")
    company_history = models.CharField(max_length=500, null=True, blank=True,
                                       verbose_name="История компании со страницы \"О компании\"")
    mission = models.CharField(max_length=100, null=True, blank=True, verbose_name="Миссия со страницы \"О компании\"")
    purposes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Цели со страницы \"О компании\"")
    description_of_services = models.CharField(max_length=100, null=True, blank=True,
                                               verbose_name="Подробное описание услуг")
    cardiology = models.CharField(max_length=100, null=True, blank=True, verbose_name="Кардиология")
    pediatrics = models.CharField(max_length=100, null=True, blank=True, verbose_name="Педиатрия")
    phone = models.CharField(max_length=11, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, verbose_name="Email")
    address = models.CharField(max_length=255, verbose_name="Адрес клиники", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь создавший этот экземпляр модели')

    # добавьте метод для получения или создания единственной записи
    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(id=1)
        return obj

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'


# Ценности (информация со страницы)
class CompanyValues(models.Model):
    """ Ценности компании (информация со страницы) """
    name = models.CharField(max_length=50, verbose_name="Название Ценности")
    description = models.CharField(max_length=100, verbose_name="Описание Ценности")

    class Meta:
        verbose_name = 'Ценность'
        verbose_name_plural = 'Ценности'


# Адрес клиники
class AddressHospital(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название адреса')
    address_line = models.CharField(max_length=255, verbose_name='Адрес',
                                    help_text='Например, г. Москва, ул. Примерная, д. 10')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.name


# Запись на приём
class Appointment(models.Model):
    """
    Модель для хранения записей пациентов на прием к врачам.

    Attributes:
        ADDRESS_CLINIC (list[tuple[str, str]]): Список адресов клиник, доступных для записи.
        address (str): Адрес клиники, выбирается из ADDRES_CLINIC.
        doctor (ForeignKey): Связь с моделью Doctors, указывающая на врача, к которому записан пациент.
        user (str): Имя пациента.
        appointment_date (datetime): Дата и время записи на прием.
        services (ForeignKey): Связь с моделью Services, указывающая на услуги, которые будут предоставлены.
    """

    address = models.ForeignKey(AddressHospital, on_delete=models.SET_NULL, verbose_name="Адрес клиники", null=True, blank=True)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name="Доктор")
    appointment_date = models.DateTimeField(verbose_name="Дата приёма")
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Услуга")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пациент')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


# Результаты диагностики
class DiagnosticResults(models.Model):
    """
    Модель для хранения результатов диагностики, связанных с записями пациентов.

    Attributes:
        appointment (ForeignKey): Связь с моделью Record, указывающая на запись, к которой относятся результаты.
        results (str): Результаты диагностики, могут быть пустыми.
    """

    appointment = models.ForeignKey(Appointment, max_length=255, verbose_name="Запись",
                                    null=True, blank=True, on_delete=models.CASCADE)
    results = models.CharField(max_length=255, verbose_name="Результаты диагностики", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь создавший этот экземпляр модели')
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name="Доктор")

    class Meta:
        verbose_name = 'Результат диагностики'
        verbose_name_plural = 'Результаты диагностики'


# Обратная связь
class Feedback(models.Model):
    subject = models.CharField(max_length=100, verbose_name="Тема обращения")
    feedback = models.CharField(max_length=500, verbose_name="Сообщение")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь создавший этот экземпляр модели')
    created_at = models.DateTimeField(default=timezone.now, help_text="Дата и время создания")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
