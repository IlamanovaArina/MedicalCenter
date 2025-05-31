from django.core.management import BaseCommand

from medical.models import CompanyValues


class Command(BaseCommand):
    help = "Добавить тестовые данные в Doctors"

    def handle(self, *args, **kwargs):
        data = [
            {
                'name': 'Оборудование',
                'description': 'Всегда в наилучшем состоянии',
            },
            {
                'name': 'Специалисты',
                'description': 'Высоко квалифицированны',
            },
            {
                'name': 'Результаты',
                'description': 'Максимально точны',
            },
        ]

        for item in data:
            CompanyValues.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
