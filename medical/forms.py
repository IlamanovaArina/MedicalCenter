from django import forms

from medical.models import Reviews, Appointment, Feedback

SPAMS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]


# Отзывы
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


# Запись на приём
class AppointmentForm(forms.ModelForm):
    """ Форма для записи на приём """

    class Meta:
        model = Appointment
        fields = ["address", "doctor", "appointment_date", "services"]
        exclude = ["user",]
        widgets = {
            "appointment_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Дата и время приёма",
                    "type": "datetime-local"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields["address"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Адрес клиники:"}
        )
        self.fields["services"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Услуга:"}
        )
        self.fields["doctor"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Доктор:"}
        )
        self.fields["appointment_date"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Дата приёма:"}
        )


# Обратная связь
class FeedbackForm(forms.ModelForm):
    """ Форма для обратной связи """

    class Meta:
        model = Feedback
        fields = ["subject", "feedback",]
        exclude = ["user", "created_at",]

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields["subject"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Возникла проблема?"}
        )
        self.fields["feedback"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Расскажите о проблеме с которой вы столкнулись."}
        )
