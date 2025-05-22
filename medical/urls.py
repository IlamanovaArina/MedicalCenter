from django.urls import path

from medical.apps import MedicalConfig
from medical.views import *

app_name = MedicalConfig.name

urlpatterns = [
    path("company/", DoctorsListView.as_view(), name="doctors"),

    path("profile/", DiagnosticListView.as_view(), name=""),

    path("contacts/", FeedbackCreateView.as_view(), name="contacts"),

    path("", HomeCreateView.as_view(), name="home"),

    path("services/", ServicesListView.as_view(), name="services"),
    path("services/<int:pk>/", ServicesDetailView.as_view(), name="services_detail"),
]
