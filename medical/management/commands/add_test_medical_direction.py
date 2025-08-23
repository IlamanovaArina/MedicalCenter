from django.core.management import BaseCommand

from medical.models import MedicalDirection


class Command(BaseCommand):
    help = "Добавить тестовые данные в MedicalDirection"

    def handle(self, *args, **kwargs):
        data = [
            {
                'name': 'Анализы крови',
                'description': 'Включают в себя большой перечень исследований.',
            },
            {
                'name': 'Онкомаркеры',
                'description': 'Обнаружение онкомаркиров в крови, мочи, и тд.',
            },
            {
                'name': 'Группа крови, Резус',
                'description': 'Исследование позволяет определить группу крови и резус-фактор.',
            },
        ]

        for item in data:
            MedicalDirection.objects.create(**item)
