from django.contrib import admin

from .models import Reviews, Doctors, Services, Information, Appointment, DiagnosticResults


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "rate", "user",)
    list_filter = ("rate",)
    search_fields = ("rate",)


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "specialization", "experience", "reviews", "user",)
    list_filter = ("last_name", "specialization", "reviews")
    search_fields = ("experience", "id",)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "user",)
    list_filter = ("name", "description",)
    search_fields = ("name", "description",)


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ("id", "text_from_the_main_page", "company_history",
                    "mission", "purposes", "phone", "address", "user",)
    list_filter = ("address",)
    search_fields = ("address",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "doctor", "appointment_date", "services", "user",)
    list_filter = ("appointment_date", "user", "services")
    search_fields = ("appointment_date", "user", "services")


@admin.register(DiagnosticResults)
class DiagnosticResultsAdmin(admin.ModelAdmin):
    list_display = ("id", "appointment", "results", "user", "doctor",)
    list_filter = ("appointment", "results",)
    search_fields = ("appointment", "results",)
