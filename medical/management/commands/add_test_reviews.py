from django.core.management import BaseCommand

from medical.models import Appointment, AddressHospital, Doctors, Services, Reviews
from users.models import User
from datetime import timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = "Добавить тестовые данные в Doctors"

    def handle(self, *args, **kwargs):
        data = [
            {
                'text': "Спасибо большое, всё прошло на высшем уровне, очередь не большая, все по записи "
                        "к своему времени.",
                'rate': "5",
                'services': Services.objects.get(id=1),
                'user': User.objects.get(id=1),
            },
            {
                'text': "Спасибо большое, всё прошло на высшем уровне, очередь не большая, все по записи "
                        "к своему времени.",
                'rate': "5",
                'services': Services.objects.get(id=1),
                'user': User.objects.get(id=1),
            },
        ]

        for item in data:
            Reviews.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
