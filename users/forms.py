from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "patronymic", "email", "avatar", "phone", "city", "country", "tg_id", "password1",
                  "password2")
        exclude = ['created_at', 'updated_at', "token", "is_active"]

    # def create_password_fields(self, *args, **kwargs):
    #     password1 = forms.CharField(verbose_name='Придумайте пароль')
    #     password2 = forms.CharField(verbose_name='Введите повторно пароль')
    #     super().create_password_fields(*args, **kwargs)

    def clean_phone_number(self):
        """ Проверка номера телефона на наличие посторонних символов """
        phone_number = self.cleaned_data.get("phone")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number

    def clean_first_name(self):
        """ Проверка имени на наличие посторонних символов """
        first_name = self.cleaned_data.get("first_name")
        if first_name and not first_name.isalpha():
            raise forms.ValidationError("Имя должно состоять только из букв.")
        return first_name

    def clean_last_name(self):
        """ Проверка фамилии на наличие посторонних символов """
        last_name = self.cleaned_data.get("last_name")
        if last_name and not last_name.isalpha():
            raise forms.ValidationError("Фамилия должно состоять только из букв.")
        return last_name

    def clean_patronymic(self):
        """ Проверка отчества на наличие посторонних символов """
        patronymic = self.cleaned_data.get("patronymic")
        if patronymic and not patronymic.isalpha():
            raise forms.ValidationError("Отчество должно состоять только из букв.")
        return patronymic

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите имя"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите фамилию"}
        )
        self.fields["patronymic"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите отчество(если есть)"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите электронную почту"}
        )
        self.fields["avatar"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Добавьте изображение"}
        )
        self.fields["phone"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите номер телефона"}
        )
        self.fields["country"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите страну проживания"}
        )
        self.fields["city"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите город проживания"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль повторно"}
        )
