from django.core.management import BaseCommand

from medical.models import Services, DiagnosticResults, Appointment
from users.models import User



class Command(BaseCommand):
    help = "Добавить тестовые данные в Doctors"

    def handle(self, *args, **kwargs):
        data = [
            {
                'appointment': Appointment.objects.get(id=1),
                'recommendations': "Рекомендации",
                'general_comments': "Общие комментарии",
                'user': User.objects.get(id=1),
            },
        ]
        for item in data:
            DiagnosticResults.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
