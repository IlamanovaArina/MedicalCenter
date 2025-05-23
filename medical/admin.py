from django.contrib import admin

from .models import *


# Направление в медицине
@admin.register(MedicalDirection)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description",)
    list_filter = ("name",)
    search_fields = ("name",)


# Отзывы
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "rate", "doctors", "services", "user",)
    list_filter = ("rate",)
    search_fields = ("rate",)


# Доктора
@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "patronymic", "medical_direction",
                    "avatar", "specialization", "experience", "user", )
    list_filter = ("last_name", "specialization", "reviews", "medical_direction",)
    search_fields = ("experience", "id", "medical_direction", )


# Услуги
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "medical_direction", "description", "price", "user",)
    list_filter = ("name", "description",)
    search_fields = ("name", "description",)


# Информация
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ("id", "text_from_the_main_page", "company_history",
                    "mission", "purposes", "description_of_services", "cardiology", "pediatrics",
                    "phone", "email", "address", "user",)
    list_filter = ("address",)
    search_fields = ("address",)


# Ценности
@admin.register(CompanyValues)
class  CompanyValuesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", )


# Адрес клиники
@admin.register(AddressHospital)
class  CompanyValuesAdmin(admin.ModelAdmin):
    list_display = ("name", "address_line", "latitude", "longitude",)


# Запись на приём
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "doctor", "appointment_date", "services", "is_active", "user",)
    list_filter = ("appointment_date", "user", "services")
    search_fields = ("appointment_date", "user", "services")


# Результаты диагностики
@admin.register(DiagnosticResults)
class DiagnosticResultsAdmin(admin.ModelAdmin):
    list_display = ("id", "appointment", "results", "user", "doctor",)
    list_filter = ("appointment", "results",)
    search_fields = ("appointment", "results",)


# Обратная связь
@admin.register(Feedback)
class  CompanyValuesAdmin(admin.ModelAdmin):
    list_display = ("subject", "feedback", "user", "created_at",)
