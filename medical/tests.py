from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import timedelta
from medical.models import (
    Doctors, MedicalDirection, Services, AddressHospital, Appointment
)
from django.utils import timezone

User = get_user_model()


class BaseTestCase(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create(
            first_name='Иван',
            last_name='Иванов',
            email='test@example.com',
            phone='89991234567',
            city='Москва',
            country='Россия',
            is_active=True
        )
        self.client = Client()
        self.client.login(email='test@gmail.com', password='testpass')

        self.med_direction = MedicalDirection.objects.create(
            name='Терапия', description='Общая терапия'
        )
        self.doctor = Doctors.objects.create(
            first_name='Иван', last_name='Иванов', patronymic='Иванович',
            specialization='Терапевт', experience='10 лет',
            medical_direction=self.med_direction,
            user=self.user
        )
        self.service = Services.objects.create(
            name='Общий анализ крови',
            medical_direction=self.med_direction,
            description='Анализ крови',
            price=500,
            user=self.user
        )
        self.address = AddressHospital.objects.create(
            name='Центральная клиника',
            address_line='г. Москва, ул. Примерная, д. 10',
        )
        self.appointment_time = timezone.now() + timedelta(days=1)
        self.appointment = Appointment.objects.create(
            address=self.address,
            doctor=self.doctor,
            services=self.service,
            appointment_date=self.appointment_time,
            user=self.user
        )


class ViewsTests(BaseTestCase):

    def test_doctors_list_view(self):
        url = reverse('medical:doctors')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Иван')

    def test_services_list_view(self):
        url = reverse('medical:services')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Общий анализ крови')

    def test_diagnostic_list_view_get(self):
        url = reverse('medical:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('diagnostic_results', response.context)
