from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from medical.models import DiagnosticResults, Doctors, Information, Appointment, Reviews, Services


#################### Reviews Views  ####################


class ReviewsCreateView(CreateView):
    model = Reviews
    # template_name = "reviews_create.html"
    fields = ['first_name', 'last_name', 'specialization']
    # success_url = reverse_lazy("medical:doctors_form")


class ReviewsDetailView(DetailView):
    model = Reviews
    # template_name = "reviews_detail.html"
    context_object_name = "reviews"


class ReviewsListView(ListView):
    model = Reviews
    # fields = ['first_name', 'last_name', 'specialization']
    # template_name = "../templates/reviews/reviews_form.html"
    context_object_name = "reviews"


class ReviewsUpdateView(UpdateView):
    model = Reviews
    # template_name = "reviews_update.html"
    # fields = ['first_name', 'last_name', 'specialization']


class ReviewsDeleteView(DeleteView):
    model = Reviews
    # template_name = "reviews_delete.html"
    # success_url = reverse_lazy("mvita:reviews_form")


#################### Doctors Views  ####################


class DoctorsCreateView(CreateView):
    model = Doctors
    template_name = "base.html"
    # template_name = "../templates/doctors/doctors_create.html"
    # fields = ["first_name", "last_name", "specialization"]
    # success_url = reverse_lazy("mvita:doctors_form")


class DoctorsDetailView(DetailView):
    model = Doctors
    # template_name = "../templates/doctors/doctors_detail.html"
    # context_object_name = "doc"


class DoctorsListView(ListView):
    model = Doctors
    # fields = ["first_name", "last_name", "specialization"]
    # template_name = "../templates/doctors/doctors_form.html"
    # context_object_name = "doctors"


class DoctorsUpdateView(UpdateView):
    model = Doctors
    # template_name = "../templates/doctors/doctors_update.html"
    # fields = ["first_name", "last_name", "specialization"]


class DoctorsDeleteView(DeleteView):
    model = Doctors
    # template_name = "../templates/doctors/doctors_delete.html"
    # success_url = reverse_lazy("mvita:doctors_form")


#################### Services Views  ####################


class ServicesCreateView(CreateView):
    model = Services
    # template_name = "services_create.html"
    # success_url = reverse_lazy("mvita:services_form")


class ServicesDeleteView(DeleteView):
    model = Services
    # template_name = "services_delete.html"
    # success_url = reverse_lazy("mvita:services_form")


class ServicesListView(ListView):
    model = Services
    # template_name = "services_form.html"
    # context_object_name = "services"


class ServicesUpdateView(UpdateView):
    model = Services
    # template_name = "services_update.html"


class ServicesDetailView(DetailView):
    model = Services
    # template_name = "services_detail.html"
    # context_object_name = "services"


#################### Information Views  ####################


class InformationCreateView(CreateView):
    model = Information
    # template_name = "information_create.html"
    # success_url = reverse_lazy("mvita:information_form")


class InformationDetailView(DetailView):
    model = Information
    # template_name = "information_detail.html"
    # context_object_name = "info"


class InformationListView(ListView):
    model = Information
    # template_name = "information_form.html"
    # success_url = reverse_lazy("mvita:information_form")
    # context_object_name = "info"


class InformationUpdateView(UpdateView):
    model = Information
    # template_name = "information_update.html"


class InformationDeleteView(DeleteView):
    model = Information
    # template_name = "information_delete.html"
    # success_url = reverse_lazy("mvita:information_form")


#################### Appointment Views  ####################


class AppointmentCreateView(CreateView):
    model = Appointment
    # template_name = "record_create.html"
    # success_url = reverse_lazy("mvita:record_form")


class AppointmentListView(ListView):
    model = Appointment
    # template_name = "record_form.html"
    # context_object_name = "record"


class AppointmentDetailView(DetailView):
    model = Appointment
    # template_name = "record_detail.html"
    # context_object_name = "record"


class AppointmentUpdateView(UpdateView):
    model = Appointment
    # template_name = "record_update.html"


class AppointmentDeleteView(DeleteView):
    model = Appointment
    # template_name = "record_delete.html"
    # success_url = reverse_lazy("mvita:record_form")


#################### DiagnosticResults Views  ####################


class DiagnosticCreateView(CreateView):
    model = DiagnosticResults
    # template_name = "diagnostic_create.html"
    # success_url = reverse_lazy("mvita:diagnostic_form")


class DiagnosticDetailView(DetailView):
    model = DiagnosticResults
    # template_name = "diagnostic_detail.html"
    # context_object_name = "record"


class DiagnosticListView(ListView):
    model = DiagnosticResults
    # template_name = "diagnostic_form.html"
    # context_object_name = "record"


class DiagnosticUpdateView(UpdateView):
    model = DiagnosticResults
    # template_name = "diagnostic_update.html"


class DiagnosticDeleteView(DeleteView):
    model = DiagnosticResults
    # template_name = "diagnostic_delete.html"
    # success_url = reverse_lazy("mvita:diagnostic_form")
