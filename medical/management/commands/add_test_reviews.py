from django.core.management import BaseCommand

from medical.models import Services, Reviews
from users.models import User


class Command(BaseCommand):
    help = "Добавить тестовые данные в Reviews"

    def handle(self, *args, **kwargs):
        data = [
            {
                'text': "Спасибо большое, всё прошло на высшем уровне, очередь не большая, все по записи "
                        "к своему времени.",
                'rate': "5",
                'services': Services.objects.get(id=1),
                'user': User.objects.get(email="admin2@gmail.com"),
            },
            {
                'text': "Спасибо большое, всё прошло на высшем уровне, очередь не большая, все по записи "
                        "к своему времени.",
                'rate': "5",
                'services': Services.objects.get(id=1),
                'user': User.objects.get(email="admin2@gmail.com"),
            },
        ]

        for item in data:
            Reviews.objects.create(**item)
