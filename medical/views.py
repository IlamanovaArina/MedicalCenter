from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from medical.forms import FeedbackForm, AppointmentForm
from medical.models import DiagnosticResults, Doctors, Information, Appointment, Reviews, Services, CompanyValues, \
    Feedback, MedicalDirection, AddressHospital


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
        context['reviews'] = Reviews.objects.all()
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
    success_url = reverse_lazy('medical:profile')

    def form_valid(self, form):
        """ Обрабатывает валидные данные формы. Устанавливаем пользователя на текущего авторизованного """
        # Устанавливаем владельца на текущего авторизованного пользователя
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        context['medical_direction'] = MedicalDirection.objects.all()
        context['address_hospital'] = AddressHospital.objects.all()
        return context


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


class DiagnosticResultDetailView(DetailView):
    model = Appointment
    template_name = 'diagnostic_result_detail.html'
    pk_url_kwarg = 'pk'  # по умолчанию, можно не указывать

    def get_object(self):
        # Получаем объект Appointment по pk из URL
        appointment = super().get_object()
        return appointment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointment = self.object

        # Получаем связанный DiagnosticResults
        try:
            results = DiagnosticResults.objects.get(appointment=appointment)
        except DiagnosticResults.DoesNotExist:
            results = None

        context['appointment'] = appointment
        context['results'] = results
        return context

#
# class ReviewsListView(ListView):
#     model = Reviews
#     template_name = 'reviews_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reviews'] = Reviews.objects.all()
#         return context
