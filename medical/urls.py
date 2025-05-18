from django.urls import path

from medical.apps import MedicalConfig
from medical.views import *

app_name = MedicalConfig.name

urlpatterns = [
    path("doctors/", DoctorsListView.as_view(), name="doctors"),
    path("<int:pk>/", DoctorsDetailView.as_view(), name="doctors_detail"),
    path("new/", DoctorsCreateView.as_view(), name="doctors_create"),
    path("<int:pk>/edit/", DoctorsUpdateView.as_view(), name="doctors_edit"),
    path("<int:pk>/delete/", DoctorsDeleteView.as_view(), name="doctors_delete"),

    path("diagnostic/", DiagnosticListView.as_view()),
    path("diagnostic/<int:pk>/", DiagnosticDetailView.as_view(), name="diagnostic_detail"),
    path("diagnostic/new/", DiagnosticCreateView.as_view(), name="diagnostic_create"),
    path("diagnostic/<int:pk>/edit/", DiagnosticUpdateView.as_view(), name="diagnostic_edit"),
    path("diagnostic/<int:pk>/delete/", DiagnosticDeleteView.as_view(), name="diagnostic_delete"),

    path("information/", InformationListView.as_view()),
    path("information/<int:pk>/", InformationDetailView.as_view(), name="information_detail"),
    path("information/new/", InformationCreateView.as_view(), name="information_create"),
    path("information/<int:pk>/edit/", InformationUpdateView.as_view(), name="information_edit"),
    path("information/<int:pk>/delete/", InformationDeleteView.as_view(), name="information_delete"),

    path("record/", AppointmentListView.as_view()),
    path("record/<int:pk>/", AppointmentDetailView.as_view(), name="record_detail"),
    path("record/new/", AppointmentCreateView.as_view(), name="record_create"),
    path("record/<int:pk>/edit/", AppointmentUpdateView.as_view(), name="record_edit"),
    path("record/<int:pk>/delete/", AppointmentDeleteView.as_view(), name="record_delete"),

    path("reviews/", ReviewsListView.as_view()),
    path("reviews/<int:pk>/", ReviewsDetailView.as_view(), name="reviews_detail"),
    path("reviews/new/", ReviewsCreateView.as_view(), name="reviews_create"),
    path("reviews/<int:pk>/edit/", ReviewsUpdateView.as_view(), name="reviews_edit"),
    path("reviews/<int:pk>/delete/", ReviewsDeleteView.as_view(), name="reviews_delete"),

    path("services/", ServicesListView.as_view()),
    path("services/<int:pk>/", ServicesDetailView.as_view(), name="services_detail"),
    path("services/new/", ServicesCreateView.as_view(), name="services_create"),
    path("services/<int:pk>/edit/", ServicesUpdateView.as_view(), name="services_edit"),
    path("services/<int:pk>/delete/", ServicesDeleteView.as_view(), name="services_delete"),

]
