import os
from django.core.files import File
from django.core.management import BaseCommand

from medical.models import Doctors, MedicalDirection


class Command(BaseCommand):
    help = "Добавить тестовые данные в Doctors"

    def handle(self, *args, **kwargs):
        image_path = os.path.join('static', 'images', 'doctor1.jpg')
        with open(image_path, 'rb') as f:
            django_file = File(f)

            data = [
                {
                    'first_name': 'Иван',
                    'last_name': 'Иванов',
                    'avatar': django_file,
                    'specialization': 'Директор, врач-диагност',
                    'medical_direction': MedicalDirection.objects.get(id=2),
                    'experience': '30 лет',
                },
                {
                    'first_name': 'Петр',
                    'last_name': 'Петров',
                    'avatar': django_file,
                    'specialization': 'Врач-гематолог',
                    'medical_direction': MedicalDirection.objects.get(id=1),
                    'experience': '8 лет',
                },
                {
                    'first_name': 'Григорий',
                    'last_name': 'Зайцев',
                    'avatar': django_file,
                    'specialization': 'Врач-гематолог',
                    'medical_direction': MedicalDirection.objects.get(id=3),
                    'experience': '10 лет',
                },
                {
                    'first_name': 'Наталья',
                    'last_name': 'Зайцева',
                    'avatar': django_file,
                    'specialization': 'Лабораторный врач',
                    'medical_direction': MedicalDirection.objects.get(id=2),
                    'experience': '11 лет',
                },
            ]

            for item in data:
                Doctors.objects.create(**item)

            self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
