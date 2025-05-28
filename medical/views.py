from django.urls import reverse_lazy
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView, View

from medical.forms import FeedbackForm, AppointmentForm
from medical.models import DiagnosticResults, Doctors, Information, Appointment, Reviews, Services, CompanyValues, \
    Feedback, MedicalDirection, AddressHospital
from django.shortcuts import get_object_or_404, redirect, render


class DoctorsListView(ListView):
    """  """
    model = Doctors
    template_name = "about_the_company.html"
    context_object_name = "doctors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_values'] = CompanyValues.objects.all()

        # Группируем по 3
        doctors = list(Doctors.objects.all())
        grouped_doctors = [doctors[i:i + 3] for i in range(0, len(doctors), 3)]
        context['grouped_doctors'] = grouped_doctors
        return context


class ServicesListView(ListView):
    """  """
    model = Services
    template_name = "services.html"
    context_object_name = "services"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medical_directions'] = MedicalDirection.objects.prefetch_related('services').all()
        # Группируем по 3
        reviews = list(Reviews.objects.all())
        grouped_reviews = [reviews[i:i + 3] for i in range(0, len(reviews), 3)]
        context['grouped_reviews'] = grouped_reviews
        return context


class InformationListView(ListView):
    """  """
    model = Information
    template_name = "contacts.html"


class DiagnosticListView(CreateView):
    """  """
    model = DiagnosticResults
    template_name = "profile.html"
    form_class = AppointmentForm
    success_url = reverse_lazy('medical:profile')

    def form_valid(self, form):
        """ Обрабатывает валидные данные формы. Устанавливаем пользователя на текущего авторизованного """
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Если пользователь авторизован, отображаются данные его профиля и остальное на странице.
         Если не авторизован, отображаются формы: "Вход", "Регистрация" """
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context["appointments"] = Appointment.objects.filter(user=user)
            context["diagnostic_results"] = DiagnosticResults.objects.filter(user=user)
        else:
            context["appointments"] = None
            context["diagnostic_results"] = None
        return context


class FeedbackCreateView(CreateView):
    """  """
    model = Feedback
    template_name = "contacts.html"
    form_class = FeedbackForm

    def form_valid(self, form):
        """ Обрабатывает валидные данные формы. Устанавливаем пользователя на текущего авторизованного """
        # Устанавливаем владельца на текущего авторизованного пользователя
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_hospitals'] = AddressHospital.objects.all()
        return context


class HomeCreateView(CreateView):
    """  """
    model = Information
    template_name = "home.html"
    form_class = FeedbackForm
    # success_url = reverse_lazy('medical:profile')

    def form_valid(self, form):
        """ Обрабатывает валидные данные формы. Устанавливаем пользователя на текущего авторизованного """
        # Устанавливаем владельца на текущего авторизованного пользователя
        form.instance.user = self.request.user
        form.save()
        super().form_valid(form)
        return render(self.request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        context['medical_direction'] = MedicalDirection.objects.all()
        context['address_hospital'] = AddressHospital.objects.all()
        return context

    # def post(self, request, *args, **kwargs):
    #     """ При нажатии на кнопку 'отправить', отправляется сообщение об успешном   """
    #     appointment_id = request.POST.get('id')
    #     appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    #
    #     # Здесь происходит отправка рассылки
    #     send_mail(
    #         f"Вы успешно записались на приём в нашей клинике: \"Сила здоровья\".",
    #         f"Вы записались на приём на {appointment.appointment_date}; по адресу: {appointment.address}; "
    #         f"на услугу: {appointment.services}; к врачу: {appointment.doctor}",
    #         EMAIL_HOST_USER,
    #         appointment.user.email
    #     )
    #
    #     return redirect('mailing:home')  # Перенаправьте на нужный URL после отправки


class AppointmentCreateView(CreateView):
    model = Appointment
    template_name = "appointment.html"
    form_class = AppointmentForm
    success_url = reverse_lazy('medical:services')

    def form_valid(self, form):
        """ Обрабатывает валидные данные формы. Устанавливаем пользователя на текущего авторизованного """
        # Устанавливаем владельца на текущего авторизованного пользователя
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


def diagnostic_results_detail(request, pk):
    """  """
    appointment = get_object_or_404(Appointment, id=pk)
    diagnosticresults = get_object_or_404(DiagnosticResults, appointment=pk)
    # Проверка, что у записи есть результаты
    try:
        results = diagnosticresults
    except DiagnosticResults.DoesNotExist:
        results = None
    return render(request, 'diagnostic_result_detail.html', {
        'appointment': appointment,
        'results': results,
    })
