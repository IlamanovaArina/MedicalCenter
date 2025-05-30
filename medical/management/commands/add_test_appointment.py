from django.core.management import BaseCommand

from medical.models import Appointment, AddressHospital, Doctors, Services
from users.models import User
from datetime import timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = "Добавить тестовые данные в Doctors"

    def handle(self, *args, **kwargs):
        data = [
            {
                'status': 'completed',
                'address': AddressHospital.objects.get(id=1),
                'doctor': Doctors.objects.get(id=1),
                'services': Services.objects.get(id=4),
                'appointment_date': timezone.now() - timedelta(days=1),
                'user': User.objects.get(id=1),
            },
            {
                'status': 'pending',
                'address': AddressHospital.objects.get(id=2),
                'doctor': Doctors.objects.get(id=2),
                'services': Services.objects.get(id=1),
                'appointment_date': timezone.now() + timedelta(days=120),
                'user': User.objects.get(id=1),
            },
        ]

        for item in data:
            Appointment.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
