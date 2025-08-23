from .models import MedicalDirection, Reviews, Doctors, Services, Information, CompanyValues, Appointment, \
    DiagnosticResults, TestResult, Feedback

from django.contrib import admin
from .models import AddressHospital
from .utils import get_coordinates


@admin.action(description='Обновить координаты выбранных адресов')
def update_coordinates(modeladmin, request, queryset):
    """ Функция, которая позволяет в админке добавлять адреса,
    а широта и долгота подставляются благодаря функции 'get_coordinates' """
    for address in queryset:
        full_address = address.address_line
        lat, lon = get_coordinates(full_address)
        if lat and lon:
            address.latitude = lat
            address.longitude = lon
            address.save()
    modeladmin.message_user(request, "Координаты успешно обновлены.")


# Адрес клиники
@admin.register(AddressHospital)
class AddressHospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address_line', 'latitude', 'longitude')
    actions = [update_coordinates]


# Направление в медицине
@admin.register(MedicalDirection)
class MedicalDirectionAdmin(admin.ModelAdmin):
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
    list_display = ("id", "text_from_the_main_page", "image_the_main_page", "company_history",
                    "mission", "purposes", "image_from_the_company", "phone", "email", "address", "user",)
    list_filter = ("address",)
    search_fields = ("address",)


# Ценности
@admin.register(CompanyValues)
class CompanyValuesAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


# Запись на приём
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "address", "doctor", "appointment_date", "services", "is_active", "user",)
    list_filter = ("appointment_date", "user", "services")
    search_fields = ("appointment_date", "user", "services")


# Результаты диагностики
@admin.register(DiagnosticResults)
class DiagnosticResultsAdmin(admin.ModelAdmin):
    list_display = ("id", "appointment", "recommendations", "user", "general_comments",)
    list_filter = ("appointment",)
    search_fields = ("appointment",)


# Медицинские тесты. Результаты
@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ("id", "diagnostic_result", "name", "value", "norm", "comment",)
    list_filter = ("name",)
    search_fields = ("name",)


# Обратная связь
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("subject", "feedback", "user", "created_at",)
