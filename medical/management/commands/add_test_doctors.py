import os
from django.core.files import File
from django.core.management import BaseCommand

from medical.models import Doctors, MedicalDirection


class Command(BaseCommand):
    help = "Добавить тестовые данные в Doctors"

    def handle(self, *args, **kwargs):
        with open(os.path.join('static', 'images', 'doctor1.jpg'), 'rb') as f1, \
                open(os.path.join('static', 'images', 'doctor2.webp'), 'rb') as f2, \
                open(os.path.join('static', 'images', 'doctor3.webp'), 'rb') as f3, \
                open(os.path.join('static', 'images', 'doctor4.png'), 'rb') as f4:
            doctor1 = File(f1)
            doctor2 = File(f2)
            doctor3 = File(f3)
            doctor4 = File(f4)

            data = [
                {
                    'first_name': 'Иван',
                    'last_name': 'Иванов',
                    'avatar': doctor1,
                    'specialization': 'Директор, врач-диагност',
                    'medical_direction': MedicalDirection.objects.get(id=2),
                    'experience': '30 лет',
                },
                {
                    'first_name': 'Петр',
                    'last_name': 'Петров',
                    'avatar': doctor2,
                    'specialization': 'Врач-гематолог',
                    'medical_direction': MedicalDirection.objects.get(id=1),
                    'experience': '8 лет',
                },
                {
                    'first_name': 'Григорий',
                    'last_name': 'Зайцев',
                    'avatar': doctor3,
                    'specialization': 'Врач-гематолог',
                    'medical_direction': MedicalDirection.objects.get(id=3),
                    'experience': '10 лет',
                },
                {
                    'first_name': 'Наталья',
                    'last_name': 'Зайцева',
                    'avatar': doctor4,
                    'specialization': 'Лабораторный врач',
                    'medical_direction': MedicalDirection.objects.get(id=2),
                    'experience': '11 лет',
                },
            ]

            for item in data:
                Doctors.objects.create(**item)
