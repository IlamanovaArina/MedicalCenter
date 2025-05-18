from django import forms

from medical.models import Reviews, Doctors, Services, Information, Appointment, DiagnosticResults

SPAMS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]


class ReviewsForm(forms.ModelForm):
    """ Форма для оставления отзыва пользователем """

    class Meta:
        model = Reviews
        fields = ["text", "rate"]
        exclude = ["user",]

    def __init__(self, *args, **kwargs):
        super(ReviewsForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Оставьте ваш отзыв:"}
        )
        self.fields["rate"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Оценка:"}
        )

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text').lower()
        for spam in SPAMS:
            if spam in text:
                self.add_error('text', f'Отзыв не может содержать спам. Вы ввели: {spam}')
        return text


class DoctorsForm(forms.ModelForm):
    """ Форма для добавления нового врача в базу данных """

    class Meta:
        model = Doctors
        fields = ["first_name", "last_name", "specialization", "experience", "reviews", ]
        exclude = ["user", ]

    def __init__(self, *args, **kwargs):
        super(DoctorsForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Имя:"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Фамилия:"}
        )
        self.fields["specialization"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Специальность:"}
        )
        self.fields["experience"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Стаж работы:"}
        )
        self.fields["reviews"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Отзывы на врача:"}
        )


class ServicesForm(forms.ModelForm):
    """ Форма для хранения информации о медицинских услугах """

    class Meta:
        model = Services
        fields = ["name", "description"]
        exclude = ["user",]

    def __init__(self, *args, **kwargs):
        super(ServicesForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Название услуги:"}
        )
        self.fields["rate"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Описание услуги:"}
        )


class InformationForm(forms.ModelForm):
    """ Форма для хранения контактной информации клиники """

    class Meta:
        model = Information
        fields = ["phone", "address", "information"]
        exclude = ["user",]

    def __init__(self, *args, **kwargs):
        super(InformationForm, self).__init__(*args, **kwargs)
        self.fields["phone"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Номер телефона:"}
        )
        self.fields["address"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Адрес клиники:"}
        )
        self.fields["information"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Главная информация:"}
        )


class AppointmentForm(forms.ModelForm):
    """ Форма для хранения контактной информации клиники """

    class Meta:
        model = Appointment
        fields = ["address", "doctor", "appointment_date", "services"]
        exclude = ["user",]

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields["address"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Адрес клиники:"}
        )
        self.fields["doctor"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Доктор:"}
        )
        self.fields["appointment_date"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Дата приёма:"}
        )
        self.fields["services"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Услуга:"}
        )


class DiagnosticResultsForm(forms.ModelForm):
    """ Форма для оставления отзыва пользователем """

    class Meta:
        model = DiagnosticResults
        fields = ["appointment", "results"]
        exclude = ["user",]

    def __init__(self, *args, **kwargs):
        super(DiagnosticResultsForm, self).__init__(*args, **kwargs)
        self.fields["appointment"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Запись:"}
        )
        self.fields["results"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Результаты диагностики:"}
        )
