from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "patronymic",
                    "email", "avatar", "phone", "city", "country", "is_active", "tg_id")
    list_filter = ("city", "country", "first_name", "last_name", "patronymic")
    search_fields = ("city", "last_name", "phone")
