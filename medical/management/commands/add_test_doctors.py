from django.core.management import BaseCommand

from medical.models import Doctors


class Command(BaseCommand):
    help = "Добавляет данные в таблицу Doctors"

    def handle(self, *args, **kwargs):
        # Пример добавления одного объекта
        my_instance_1 = Doctors(
            first_name='Иван',
            last_name='Иванов',
            avatar="https://i.pinimg.com/originals/45/97/94/4597946c55acfcc87590840d90c0379b.jpg",
            specialization='Директор, врач-диагност',
            experience='15 года',
        )
        my_instance_1.save()

        my_instance_2 = Doctors(
            first_name='Петр',
            last_name='Петров',
            avatar="https://i.pinimg.com/736x/6d/90/9e/6d909ef2722a62dc868e88a4977eea2b.jpg",
            specialization='Врач функциональной диагностики',
            experience='8 года',
        )
        my_instance_2.save()

        my_instance_3 = Doctors(
            first_name='Григорий',
            last_name='Зайцев',
            avatar="https://avatars.mds.yandex.net/i?id=73aa22109ead27d05fdccd30eae699fa_l-12485500-images-thumbs&n=13",
            specialization='Врач ультразвуковой диагностики',
            experience='10 года',
        )
        my_instance_3.save()

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))