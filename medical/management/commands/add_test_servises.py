from django.core.management import BaseCommand
from medical.models import Services, MedicalDirection


class Command(BaseCommand):
    help = "Добавить тестовые данные в Services"

    def handle(self, *args, **kwargs):
        data = [
            {
                'name': 'Общий анализ крови',
                'medical_direction': MedicalDirection.objects.get(id=1),
                'description': 'Быстрый и точный анализ для оценки общего состояния организма.',
                'price': '1500'
            },
            {
                'name': 'Анализ группы крови',
                'medical_direction': MedicalDirection.objects.get(id=3),
                'description': 'Лабораторное исследование крови, которое помогает определить общее состояние организма и диагностировать различные заболевания.',
                'price': '800'
            },
            {
                'name': 'Антитела к антигенам эритроцитов',
                'medical_direction': MedicalDirection.objects.get(id=3),
                'description': 'Это лабораторное определение титра иммуноглобулинов.',
                'price': '800'
            },
            {
                'name': 'Онкомаркеры в крови',
                'medical_direction': MedicalDirection.objects.get(id=2),
                'description': 'Метод лабораторного исследования, используемый в диагностике онкологических '
                        '(раковых) заболеваний.',
                'price': '800'
            },
            {
                'name': 'Онкомаркеры в моче',
                'medical_direction': MedicalDirection.objects.get(id=2),
                'description': 'Метод лабораторного исследования, используемый в диагностике онкологических '
                        '(раковых) заболеваний.',
                'price': '800'
            },
            # добавьте сколько нужно
        ]

        for item in data:
            Services.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
