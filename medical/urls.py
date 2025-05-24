from django.urls import path
from . import views

from medical.apps import MedicalConfig
from medical.views import *

app_name = MedicalConfig.name

urlpatterns = [
    path("company/", DoctorsListView.as_view(), name="doctors"),

    path("profile/", DiagnosticListView.as_view(), name="profile"),

    path("contacts/", FeedbackCreateView.as_view(), name="contacts"),

    path("", HomeCreateView.as_view(), name="home"),

    path("services/", ServicesListView.as_view(), name="services"),

    path("appointment/", AppointmentCreateView.as_view(), name="appointment"),

    # path("result/<int:pk>/", DiagnosticResultsDetailView.as_view(), name="result"),

    path('result/<int:pk>/', views.diagnostic_results_detail, name='diagnostic_results_detail')

]
