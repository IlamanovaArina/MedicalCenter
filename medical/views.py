from django.urls import reverse_lazy
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView, View

from medical.forms import FeedbackForm
from medical.models import DiagnosticResults, Doctors, Information, Appointment, Reviews, Services, CompanyValues, \
    Feedback
from django.shortcuts import get_object_or_404, redirect


# Reviews Views


# class ReviewsCreateView(CreateView):
#     model = Reviews
#     # template_name = "reviews_create.html"
#     fields = ['first_name', 'last_name', 'specialization']
#     # success_url = reverse_lazy("medical:doctors_form")
#
#
# class ReviewsDetailView(DetailView):
#     model = Reviews
#     # template_name = "reviews_detail.html"
#     context_object_name = "reviews"
#
#
# class ReviewsListView(ListView):
#     model = Reviews
#     # fields = ['first_name', 'last_name', 'specialization']
#     # template_name = "../templates/reviews/reviews_form.html"
#     context_object_name = "reviews"
#
#
# class ReviewsUpdateView(UpdateView):
#     model = Reviews
#     # template_name = "reviews_update.html"
#     # fields = ['first_name', 'last_name', 'specialization']
#
#
# class ReviewsDeleteView(DeleteView):
#     model = Reviews
#     # template_name = "reviews_delete.html"
#     # success_url = reverse_lazy("mvita:reviews_form")
#
#
# # Doctors Views
#
#
# class DoctorsCreateView(CreateView):
#     model = Doctors
#     template_name = "base.html"
#     # template_name = "../templates/doctors/doctors_create.html"
#     # fields = ["first_name", "last_name", "specialization"]
#     # success_url = reverse_lazy("mvita:doctors_form")
#
#
# class DoctorsDetailView(DetailView):
#     model = Doctors
#     # template_name = "../templates/doctors/doctors_detail.html"
#     # context_object_name = "doc"


class DoctorsListView(ListView):
    model = Doctors
    template_name = "about_the_company.html"
    context_object_name = "doctors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['information'] = Information.get_solo()
        context['company_values'] = CompanyValues.objects.all()
        return context


# class DoctorsUpdateView(UpdateView):
#     model = Doctors
#     # template_name = "../templates/doctors/doctors_update.html"
#     # fields = ["first_name", "last_name", "specialization"]
#
#
# class DoctorsDeleteView(DeleteView):
#     model = Doctors
#     # template_name = "../templates/doctors/doctors_delete.html"
#     # success_url = reverse_lazy("mvita:doctors_form")
#
#
# # Services Views
#
#
# class ServicesCreateView(CreateView):
#     model = Services
#     # template_name = "services_create.html"
#     # success_url = reverse_lazy("mvita:services_form")
#
#
class ServicesDetailView(DetailView):
    model = Services
    template_name = "services_detail.html"
    context_object_name = "service"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = list(Reviews.objects.all())
        # Группируем по 3
        grouped_reviews = [reviews[i:i + 3] for i in range(0, len(reviews), 3)]
        context['grouped_reviews'] = grouped_reviews
        return context


class ServicesListView(ListView):
    model = Services
    template_name = "services.html"
    context_object_name = "services"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['information'] = Information.get_solo()
        return context


# class ServicesUpdateView(UpdateView):
#     model = Services
#     # template_name = "services_update.html"
#
#
# class ServicesDeleteView(DeleteView):
#     model = Services
#     # template_name = "services_delete.html"
#     # success_url = reverse_lazy("mvita:services_form")
#
#
# # Information Views
#
#
# class InformationCreateView(CreateView):
#     model = Information
#     # template_name = "information_create.html"
#     # success_url = reverse_lazy("mvita:information_form")
#
#
# class InformationDetailView(DetailView):
#     model = Information
#     # template_name = "information_detail.html"
#     # context_object_name = "info"


class InformationListView(ListView):
    model = Information
    template_name = "contacts.html"



# class InformationUpdateView(UpdateView):
#     model = Information
#     # template_name = "information_update.html"
#
#
# class InformationDeleteView(DeleteView):
#     model = Information
#     # template_name = "information_delete.html"
#     # success_url = reverse_lazy("mvita:information_form")


# Appointment Views


# class AppointmentCreateView(CreateView):
#     model = Appointment
    # template_name =
#
#
# class AppointmentListView(ListView):
#     model = Appointment
#     # template_name = "record_form.html"
#     # context_object_name = "record"
#
#
# class AppointmentDetailView(DetailView):
#     model = Appointment
#     # template_name = "record_detail.html"
#     # context_object_name = "record"
#
#
# class AppointmentUpdateView(UpdateView):
#     model = Appointment
#     # template_name = "record_update.html"
#
#
# class AppointmentDeleteView(DeleteView):
#     model = Appointment
#     # template_name = "record_delete.html"
#     # success_url = reverse_lazy("mvita:record_form")
#
#
# # DiagnosticResults Views
#
#
# class DiagnosticCreateView(CreateView):
#     model = DiagnosticResults
#     # template_name = "diagnostic_create.html"
#     # success_url = reverse_lazy("mvita:diagnostic_form")
#
#
# class DiagnosticDetailView(DetailView):
#     model = DiagnosticResults
#     # template_name = "diagnostic_detail.html"
#     # context_object_name = "record"


class DiagnosticListView(ListView):
    model = DiagnosticResults
    template_name = "profile.html"
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     current_user = self.request.user
    #     context['user'] = current_user
    #     return context

    # def get_form_kwargs(self):
    #     """
    #     Получает аргументы для формы.
    #     """
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user  # Передаем текущего пользователя в форму
    #     return kwargs


# class DiagnosticUpdateView(UpdateView):
#     model = DiagnosticResults
#     # template_name = "diagnostic_update.html"
#
#
# class DiagnosticDeleteView(DeleteView):
#     model = DiagnosticResults
#     # template_name = "diagnostic_delete.html"
#     # success_url = reverse_lazy("mvita:diagnostic_form")


class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = "contacts.html"
    form_class = FeedbackForm

    def form_valid(self, form):
        """ Обрабатывает валидные данные формы. Устанавливаем пользователя на текущего авторизованного """
        # Устанавливаем владельца на текущего авторизованного пользователя
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class HomeCreateView(CreateView):
    """  """
    model = Information
    template_name = "home.html"
    form_class = FeedbackForm

    def form_valid(self, form):
        """ Обрабатывает валидные данные формы. Устанавливаем пользователя на текущего авторизованного """
        # Устанавливаем владельца на текущего авторизованного пользователя
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        # context['information'] = Information.get_solo()
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
