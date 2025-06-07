from django.urls import path

from medical.apps import MedicalConfig
from medical.views import DoctorsListView, FeedbackCreateView, DiagnosticListView, HomeCreateView, ServicesListView, \
    AppointmentCreateView, DiagnosticResultDetailView

app_name = MedicalConfig.name

urlpatterns = [
    path("company/", DoctorsListView.as_view(), name="doctors"),
    path("profile/", DiagnosticListView.as_view(), name="profile"),
    path("contacts/", FeedbackCreateView.as_view(), name="contacts"),
    path("", HomeCreateView.as_view(), name="home"),
    path("services/", ServicesListView.as_view(), name="services"),
    path("appointment/", AppointmentCreateView.as_view(), name="appointment"),
    path('result/<int:pk>/', DiagnosticResultDetailView.as_view(), name='diagnostic_result_detail'),
]
