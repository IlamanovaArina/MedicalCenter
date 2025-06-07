from django.core.management import BaseCommand
from medical.models import AddressHospital


class Command(BaseCommand):
    help = "Добавить тестовые данные в AddressHospital"

    def handle(self, *args, **kwargs):
        data = [
            {
                'name': 'Моё здоровье',
                'address_line': 'Сормовская ул., 88, Краснодар',
            },
            {
                'name': 'Орбита',
                'address_line': 'ул. Максима Горького, 32, Краснодар',
            },
        ]

        for item in data:
            AddressHospital.objects.create(**item)
