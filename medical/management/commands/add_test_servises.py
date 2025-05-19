from django.core.management import BaseCommand

from medical.models import Services


class Command(BaseCommand):
    help = "Добавляет данные в таблицу Services"

    def handle(self, *args, **kwargs):
        # Пример добавления одного объекта
        my_instance = Services(
            name='Общий анализ крови',
            description='Быстрый и точный анализ для оценки общего состояния организма.',
            price='500',
        )
        my_instance.save()
        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
