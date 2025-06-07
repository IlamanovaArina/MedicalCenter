from django.core.management import BaseCommand

from medical.models import DiagnosticResults, Appointment
from users.models import User


class Command(BaseCommand):
    help = "Добавить тестовые данные в DiagnosticResults"

    def handle(self, *args, **kwargs):
        data = [
            {
                'appointment': Appointment.objects.get(id=1),
                'recommendations': "Рекомендации",
                'general_comments': "Общие комментарии",
                'user': User.objects.get(email="admin2@gmail.com"),
            },
        ]
        for item in data:
            DiagnosticResults.objects.create(**item)
