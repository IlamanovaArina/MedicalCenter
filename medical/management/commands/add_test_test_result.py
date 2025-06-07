from django.core.management import BaseCommand

from medical.models import TestResult, DiagnosticResults


class Command(BaseCommand):
    help = "Добавить тестовые данные в TestResult"

    def handle(self, *args, **kwargs):
        data = [
            {
                'diagnostic_result': DiagnosticResults.objects.get(id=1),
                'name': 'Гемоглобин',
                'value': "110",
                'norm': '112-156',
                'comment': "Понижен",
            },
            {
                'diagnostic_result': DiagnosticResults.objects.get(id=1),
                'name': 'Гематокрит',
                'value': "44,1",
                'norm': '33,0-45,0',
                'comment': "В приделах нормы",
            },
            {
                'diagnostic_result': DiagnosticResults.objects.get(id=1),
                'name': 'Эритроциты',
                'value': "4,71",
                'norm': '3,5-5,2',
                'comment': "В приделах нормы",
            },
            {
                'diagnostic_result': DiagnosticResults.objects.get(id=1),
                'name': 'Лейкоциты',
                'value': "5,6",
                'norm': '4,0-8,8',
                'comment': "В приделах нормы",
            },
        ]

        for item in data:
            TestResult.objects.create(**item)
