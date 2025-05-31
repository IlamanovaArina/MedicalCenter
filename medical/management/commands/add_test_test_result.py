from django.core.management import BaseCommand

from medical.models import TestResult, DiagnosticResults


class Command(BaseCommand):
    help = "Добавить тестовые данные в Doctors"

    def handle(self, *args, **kwargs):
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
