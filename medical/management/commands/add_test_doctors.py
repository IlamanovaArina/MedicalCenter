import os
from django.core.files import File
from django.core.management import BaseCommand

from medical.models import Doctors


class Command(BaseCommand):
    help = "Добавляет данные в таблицу Doctors"

    def handle(self, *args, **kwargs):
        # Пример добавления одного объекта
        image_path = os.path.join('static', 'images', 'doctor1.jpg')
        with open(image_path, 'rb') as f:
            django_file = File(f)

        my_instance_1 = Doctors(
            first_name='Иван',
            last_name='Иванов',
            avatar=django_file,
            specialization='Директор, врач-диагност',
            medical_direction=1,
            experience='15 лет',
        )
        my_instance_1.save()

        my_instance_2 = Doctors(
            first_name='Петр',
            last_name='Петров',
            avatar=django_file,
            specialization='Врач функциональной диагностики',
            medical_direction=3,
            experience='8 лет',
        )
        my_instance_2.save()

        my_instance_3 = Doctors(
            first_name='Григорий',
            last_name='Зайцев',
            avatar=django_file,
            specialization='Врач ультразвуковой диагностики',
            medical_direction=2,
            experience='10 лет',
        )
        my_instance_3.save()

        my_instance_4 = Doctors(
            first_name='Наталья',
            last_name='Зайцева',
            avatar=django_file,
            specialization='Врач ультразвуковой диагностики',
            medical_direction=3,
            experience='6 лет',
        )
        my_instance_4.save()

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))