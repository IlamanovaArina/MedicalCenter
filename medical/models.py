from django.utils import timezone

from django.db import models

from config import settings
from medical.utils import get_coordinates


# Направление в медицине
class MedicalDirection(models.Model):
    """
    Модель для хранения информации о медицинских направлениях.

    Атрибуты:
        - name (CharField): Название направления, например, кардиология, неврология.
        - description (CharField): Описание направления, более подробная информация.

    Метаданные:
        - verbose_name: "Направление в медицине"
        - verbose_name_plural: "Направления в медицине"

    Методы:
        - __str__: возвращает название направления для удобства отображения.
        """
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

    Атрибуты:
        - first_name (CharField): Имя врача.
        - last_name (CharField): Фамилия врача.
        - patronymic (CharField): Отчество врача, необязательное.
        - medical_direction (ForeignKey): Связь с моделью MedicalDirection, указывающая специализацию врача.
        - avatar (ImageField): Фото врача, необязательное.
        - specialization (CharField): Специальность врача, например, терапевт, хирург.
        - experience (CharField): Стаж работы врача.
        - user (ForeignKey): Связь с пользователем, создавшим запись, необязательное.

    Метаданные:
        - verbose_name: "Доктор"
        - verbose_name_plural: "Доктора"

    Методы:
        - __str__: возвращает полное имя врача, учитывая отчество, для удобства отображения.
    """

    first_name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", null=True, blank=True)
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество")
    medical_direction = models.ForeignKey(MedicalDirection, on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name="Медицинское направление")
    avatar = models.ImageField(upload_to="medical/", blank=True, null=True, verbose_name="Фотография")
    specialization = models.CharField(max_length=255, verbose_name="Специальность", null=True, blank=True)
    experience = models.CharField(max_length=255, verbose_name="Стаж работы", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь создавший этот экземпляр модели')

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        if self.patronymic:
            return f"{self.first_name} {self.patronymic}"
        return f"{self.last_name} {self.first_name}"


# Услуги
class Services(models.Model):
    """
    Модель для хранения информации о медицинских услугах.

    Атрибуты:
        - name (CharField): Название услуги.
        - medical_direction (ForeignKey): Связь с моделью MedicalDirection, указывающая направление услуги.
        - description (CharField): Описание услуги.
        - price (IntegerField): Цена услуги, необязательное.
        - user (ForeignKey): Связь с пользователем, создавшим услугу, необязательное.

    Метаданные:
        - verbose_name: "Услуга"
        - verbose_name_plural: "Услуги"

    Методы:
        - __str__: возвращает название услуги для удобства отображения.
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

    def __str__(self):
        return self.name


# Отзывы
class Reviews(models.Model):
    """
    Модель для хранения отзывов о врачах и услугах клиники.

    Атрибуты:
        - text (CharField): Текст отзыва, необязательное.
        - rate (CharField): Оценка в виде количества звезд, выбирается из предопределенного списка.
        - doctors (ForeignKey): Связь с моделью Doctors, указывающая на врача, о котором оставлен отзыв.
        - services (ForeignKey): Связь с моделью Services, указывающая на услугу, о которой оставлен отзыв.
        - user (ForeignKey): Связь с пользователем, оставившим отзыв.

    Метаданные:
        - verbose_name: "Отзыв"
        - verbose_name_plural: "Отзывы"

    Методы:
        - __str__: возвращает текст отзыва для отображения.
    """

    DOCTOR_RATE: list[tuple[str, str]] = [
        ("5", "Все отлично!"),
        ("4", "Все хорошо."),
        ("3", "Есть замечания"),
        ("2", "Не устроило"),
        ("1", "Категорически не устроило"),
    ]

    text = models.CharField(max_length=100, verbose_name="Отзыв", blank=True, null=True)
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
    Модель для хранения контактной и общей информации о клинике.

    Атрибуты:
        - text_from_the_main_page (TextField): Информация, отображаемая на главной странице.
        - image_the_main_page (ImageField): Фото для главной страницы.
        - company_history (TextField): История компании, раздел "О компании".
        - mission (CharField): Миссия компании.
        - purposes (CharField): Цели компании.
        - image_from_the_company (ImageField): Фото из раздела "О компании".
        - phone (CharField): Контактный телефон.
        - email (EmailField): Контактный email.
        - address (CharField): Адрес центральной клиники.
        - user (ForeignKey): Пользователь, создавший запись.

    Методы:
        - get_solo: класс-метод для получения или создания единственной записи.
    """
    text_from_the_main_page = models.TextField(null=True, blank=True,
                                               verbose_name="Информация с главной страницы")
    image_the_main_page = models.ImageField(upload_to="medical/", blank=True, null=True,
                                            verbose_name="Фото с главной страницы")
    company_history = models.TextField(null=True, blank=True,
                                       verbose_name="История компании со страницы \"О компании\"")
    mission = models.CharField(max_length=100, null=True, blank=True, verbose_name="Миссия со страницы \"О компании\"")
    purposes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Цели со страницы \"О компании\"")
    image_from_the_company = models.ImageField(upload_to="medical/", blank=True, null=True,
                                               verbose_name="Фото со страницы \"О компании\"")
    phone = models.CharField(max_length=11, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, verbose_name="Email")
    address = models.CharField(max_length=255, verbose_name="Адрес центральной клиники", null=True, blank=True)
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
    """
    Модель для хранения ценностей компании (информация со страницы).

    Атрибуты:
        - name (CharField): Название ценности.
        - description (CharField): Описание ценности.

    Метаданные:
        - verbose_name: "Ценность"
        - verbose_name_plural: "Ценности"
    """
    name = models.CharField(max_length=50, verbose_name="Название Ценности")
    description = models.CharField(max_length=100, verbose_name="Описание Ценности")

    class Meta:
        verbose_name = 'Ценность'
        verbose_name_plural = 'Ценности'


# Адрес клиники
class AddressHospital(models.Model):
    """
     Модель для хранения информации об адресах клиники.

    Атрибуты:
        - name (CharField): Название адреса.
        - address_line (CharField): Полный адрес, например, "г. Москва, ул. Примерная, д. 10".
        - reception_phone (CharField): Номер телефона для приема, необязательное.
        - latitude (FloatField): Широта, вычисляется автоматически при сохранении, если не указана.
        - longitude (FloatField): Долгота, вычисляется автоматически при сохранении, если не указана.

    Методы:
        - save: переопределен для автоматического получения координат по адресу.
        - __str__: возвращает строковое представление в виде "Название, Адрес".
    """
    name = models.CharField(max_length=255, verbose_name='Название адреса')
    address_line = models.CharField(max_length=255, verbose_name='Адрес',
                                    help_text='Например, г. Москва, ул. Примерная, д. 10')
    reception_phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="Номер телефона", )
    latitude = models.FloatField(verbose_name='Широта', null=True, blank=True, )
    longitude = models.FloatField(verbose_name='Долгота', null=True, blank=True, )

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            lat, lon = get_coordinates(self.address_line)
            if lat and lon:
                self.latitude = lat
                self.longitude = lon
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}, {self.address_line}"


# Запись на приём
class Appointment(models.Model):
    """
    Модель для хранения записей пациентов на прием к врачам.

    Атрибуты:
        - status (CharField): Статус записи, например, "в ожидании" или "услуга оказана".
        - address (ForeignKey): Связь с моделью AddressHospital, указывающая на адрес клиники.
        - doctor (ForeignKey): Связь с моделью Doctors, указывающая на врача, к которому записан пациент.
        - services (ForeignKey): Связь с моделью Services, указывающая на услугу, которую планируют предоставить.
        - appointment_date (DateTimeField): Дата и время приема.
        - is_active (BooleanField): Статус активности записи.
        - user (ForeignKey): Связь с пользователем (пациентом), сделавшим запись.

    Метаданные:
        - verbose_name: "Запись"
        - verbose_name_plural: "Записи"

    Методы:
        - __str__: возвращает строковое представление записи, включающее адрес, врача или услугу, пациента и дату.
    """
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'В ожидании'),
            ('completed', 'Услуга оказана'),
            # другие статусы
        ],
        default='pending', verbose_name="Статус"
    )
    address = models.ForeignKey(AddressHospital, on_delete=models.SET_NULL, verbose_name="Адрес клиники", null=True,
                                blank=True)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name="Доктор", null=True, blank=True, )
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Услуга", null=True, blank=True, )
    appointment_date = models.DateTimeField(verbose_name="Дата приёма")
    is_active = models.BooleanField(default=True, verbose_name="Статус записи")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пациент')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        if self.doctor:
            return f"{self.address}, {self.doctor}, пациент: {self.user}, дата приёма: {self.appointment_date}"
        if self.services:
            return f"{self.address}, {self.services}, пациент: {self.user}, дата приёма: {self.appointment_date}"


# Результаты диагностики
class DiagnosticResults(models.Model):
    """
    Модель для хранения результатов диагностики, связанных с записями пациентов.

    Атрибуты:
        - appointment (ForeignKey): Связь с моделью Appointment, указывающая на конкретную запись.
        - recommendations (TextField): Рекомендации по результатам диагностики.
        - user (ForeignKey): Пользователь, создавший запись.
        - general_comments (TextField): Общие комментарии по результатам.

    Метаданные:
        - verbose_name: "Результат диагностики"
        - verbose_name_plural: "Результаты диагностики"

    Методы:
        - __str__: возвращает строковое представление, обычно — строку записи.
    """

    appointment = models.ForeignKey(Appointment, max_length=255, verbose_name="Запись",
                                    null=True, blank=True, on_delete=models.CASCADE)
    recommendations = models.TextField(blank=True, null=True, verbose_name="Рекомендации")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь создавший этот экземпляр модели')
    general_comments = models.TextField(blank=True, null=True, verbose_name="Общие комментарии")

    class Meta:
        verbose_name = 'Результат диагностики'
        verbose_name_plural = 'Результаты диагностики'

    def __str__(self):
        return f"{self.appointment}"


# Медицинские тесты. Результаты
class TestResult(models.Model):
    """
    Модель для хранения результатов медицинских тестов, связанных с диагностическими результатами.

    Атрибуты:
        - diagnostic_result (ForeignKey): Связь с моделью DiagnosticResults.
        - name (CharField): Название теста.
        - value (CharField): Значение теста.
        - norm (CharField): Нормативное значение.
        - comment (TextField): Комментарии по результатам теста.
    """
    diagnostic_result = models.ForeignKey(DiagnosticResults, related_name='tests', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название")
    value = models.CharField(max_length=255, null=True, blank=True, verbose_name="Значение")
    norm = models.CharField(max_length=255, null=True, blank=True, verbose_name="Норма")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")


# Обратная связь
class Feedback(models.Model):
    """
    Модель для хранения обратной связи и сообщений от пользователей.

    Атрибуты:
        - subject (CharField): Тема обращения.
        - feedback (CharField): Текст сообщения.
        - user (ForeignKey): Связь с пользователем, оставившим сообщение.
        - created_at (DateTimeField): Дата и время создания сообщения.

    Метаданные:
        - verbose_name: "Сообщение"
        - verbose_name_plural: "Сообщения"
    """
    subject = models.CharField(max_length=100, verbose_name="Тема обращения")
    feedback = models.CharField(max_length=500, verbose_name="Сообщение")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь создавший этот экземпляр модели')
    created_at = models.DateTimeField(default=timezone.now, help_text="Дата и время создания")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
