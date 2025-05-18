from django.db import models

from config import settings


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Пользователь, оставивший отзыв')


class Doctors(models.Model):
    """
    Модель для хранения информации о врачах.

    Attributes:
        first_name (str): Имя врача.
        last_name (str): Фамилия врача.
        specialization (str): Специальность врача.
        experience (str): Стаж работы врача.
        reviews (ForeignKey): Связь с моделью Reviews для хранения отзывов.
    """

    first_name = models.CharField(
        max_length=255, verbose_name="Имя", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255, verbose_name="Фамилия", null=True, blank=True
    )
    specialization = models.CharField(
        max_length=255, verbose_name="Специальность", null=True, blank=True
    )
    experience = models.CharField(
        max_length=255, verbose_name="Стаж работы", null=True, blank=True
    )
    reviews = models.ForeignKey(Reviews, verbose_name="Отзывы на врача",
                                null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Пользователь создавший этот экземпляр модели')


class Services(models.Model):
    """
    Модель для хранения информации о медицинских услугах.
    """

    name = models.CharField(max_length=500, verbose_name="Название услуги")
    description = models.CharField(max_length=500, verbose_name="Описание услуги")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Пользователь создавший этот экземпляр модели')


class Information(models.Model):
    """
    Модель для хранения контактной информации клиники.

    Attributes:
        phone (str): Номер телефона клиники.
        address (str): Адрес клиники.
    """

    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="Номер телефона")
    address = models.CharField(max_length=255, verbose_name="Адрес клиники", null=True, blank=True)
    information = models.TextField(max_length=500 ,verbose_name="Главная информация", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Пользователь создавший этот экземпляр модели')


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

    ADDRESS_CLINIC = [
        ("Медицинская лаборатория", "Ул.Пролетарская 28, 1 этаж"),
        ("Медицинская лаборатория", "Ул.Луначарского 308, 1 этаж"),
    ]
    address = models.CharField(max_length=255, verbose_name="Адрес клиники",
                              null=True, blank=True, choices=ADDRESS_CLINIC,)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(verbose_name="Дата приёма")
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Пациент')


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
