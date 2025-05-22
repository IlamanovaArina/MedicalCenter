from django.core.management import BaseCommand

from medical.models import Services


class Command(BaseCommand):
    help = "Добавляет данные в таблицу Services"

    def handle(self, *args, **kwargs):
        # Пример добавления одного объекта
        my_instance_1 = Services(
            name='Общий анализ крови',
            description='Быстрый и точный анализ для оценки общего состояния организма.',
            price='500',
        )
        my_instance_1.save()

        my_instance_2 = Services(
            name='Неврология',
            description='Прием врача с осмотром.',
            price='500',
        )
        my_instance_2.save()

        my_instance_3 = Services(
            name='Гинекология',
            description='Прием врача с осмотром.',
            price='500',
        )
        my_instance_3.save()

        my_instance_4 = Services(
            name='Урология',
            description='Прием врача с осмотром.',
            price='500',
        )
        my_instance_4.save()

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
