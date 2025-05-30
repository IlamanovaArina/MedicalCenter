import os
from django.core.files import File
from django.core.management import BaseCommand

from medical.models import Doctors, MedicalDirection, TestResult, DiagnosticResults


class Command(BaseCommand):
    help = "Добавить тестовые данные в Doctors"

    def handle(self, *args, **kwargs):
        image_path = os.path.join('static', 'images', 'doctor1.jpg')
        with open(image_path, 'rb') as f:
            django_file = File(f)

            data = [
                {
                    'diagnostic_result': DiagnosticResults.objects.get(id=1),
                    'name': 'Гемоглобин',
                    'value': "135",
                    'norm': '120−160',
                    'comment': "В приделах нормы",
                },
                {
                    'diagnostic_result': DiagnosticResults.objects.get(id=1),
                    'name': 'Гемоглобин',
                    'value': "135",
                    'norm': '120−160',
                    'comment': "В приделах нормы",
                },
                {
                    'diagnostic_result': DiagnosticResults.objects.get(id=1),
                    'name': 'Гемоглобин',
                    'value': "135",
                    'norm': '120−160',
                    'comment': "В приделах нормы",
                },
            ]

            for item in data:
                TestResult.objects.create(**item)

            self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
