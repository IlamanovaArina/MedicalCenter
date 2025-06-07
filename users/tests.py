from django.contrib.auth import get_user_model
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name='Иван',
            last_name='Иванов',
            email='test@example.com',
            phone='89991234567',
            city='Москва',
            country='Россия',
            is_active=True
        )

    def test_create_user(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.first_name, 'Иван')
        self.assertEqual(self.user.last_name, 'Иванов')
        self.assertTrue(self.user.is_active)
        self.assertIsNone(self.user.patronymic)

    def test_str_method(self):
        self.assertEqual(str(self.user), 'test@example.com')

    def test_unique_email(self):
        with self.assertRaises(Exception):
            User.objects.create(
                first_name='Петр',
                last_name='Петров',
                email='test@example.com'
            )

    def test_created_at_auto_now(self):
        self.assertLessEqual(self.user.created_at, timezone.now())

    def test_updated_at_auto_now(self):
        self.assertLessEqual(self.user.updated_at, timezone.now())


class RegisterViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('users:register')

    def test_get_register_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_post_register_user(self):
        data = {
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'email': 'newuser@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='newuser@example.com').exists())


class ProfileUpdateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test2@example.com',
            first_name='Иван',
            last_name='Иванов',
        )
        self.user.set_password('Password123!')
        self.user.save()
        self.client.login(email='test2@example.com', password='Password123!')
        self.update_url = reverse('users:profile_update', kwargs={'pk': self.user.pk})

    def test_get_update_page(self):
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_profile.html')

    def test_post_update_profile(self):
        data = {
            'first_name': 'Петр',
            'last_name': 'Петров',
            'email': self.user.email,
            'phone': '89991234567',
            'city': 'Москва',
            'country': 'Россия',
            'patronymic': 'Иванович',
        }
        self.client.post(self.update_url, data)

        # Проверяем, что данные обновились
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Петр')
        self.assertEqual(self.user.last_name, 'Петров')
        self.assertEqual(self.user.phone, '89991234567')
        self.assertEqual(self.user.city, 'Москва')
        self.assertEqual(self.user.country, 'Россия')
        self.assertEqual(self.user.patronymic, 'Иванович')
