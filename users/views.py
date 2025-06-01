from smtplib import SMTPSenderRefused
from django.utils import timezone

from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class RegisterView(CreateView):
    """
     Представление для регистрации нового пользователя.

    Атрибуты:
        - model (User): модель пользователя.
        - form_class (UserRegisterForm): форма для регистрации.
        - template_name (str): шаблон для отображения формы регистрации.
        - success_url (URL): URL для перенаправления после успешной регистрации.

    Методы:
        - form_valid: при успешной отправке формы сохраняет пользователя, авторизует его и отправляет приветственное письмо.
        - send_welcome_email: отправляет письмо с подтверждением регистрации. В случае ошибок возвращает URL страницы ошибки.
    """
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        try:
            subject = 'Добро пожаловать в наш сервис'
            message = 'Спасибо, что зарегистрировались в нашем сервисе!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)
        except SMTPSenderRefused:
            return reverse_lazy('users:error')
        except Exception as e:
            # Логируйте или выводите ошибку
            print(e)
            return reverse_lazy('users:error')


class ProfileUpdateView(UpdateView):
    """
    Представление для обновления профиля пользователя.

    Атрибуты:
        - model (User): модель пользователя.
        - template_name (str): шаблон для формы обновления профиля.
        - form_class (UserUpdateForm): форма для редактирования профиля.
        - success_url (URL): URL для перенаправления после успешного обновления.

    Методы:
        - form_valid: сохраняет изменения, обновляя поле `updated_at` вручную.
    """
    model = User
    template_name = "update_profile.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('medical:profile')

    def form_valid(self, form):
        # Обновляем поле updated_at вручную, если оно не обновляется автоматически
        user = form.save(commit=False)
        user.updated_at = timezone.now()
        user.save()
        return super().form_valid(form)
