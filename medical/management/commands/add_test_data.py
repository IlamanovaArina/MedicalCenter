from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Запускает все команды для заполнения тестовыми данными"

    def handle(self, *args, **kwargs):
        # Вызов ваших команд по очереди
        try:
            call_command('csu')
            self.stdout.write(self.style.SUCCESS("Админ успешно добавлен"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении админа: {e}"))

        try:
            call_command('add_test_address_hospital')
            self.stdout.write(self.style.SUCCESS("Адреса успешно добавлены"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении адресов: {e}"))

        try:
            call_command('add_test_company_values')
            self.stdout.write(self.style.SUCCESS("Ценности успешно добавлены"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении ценностей: {e}"))

        try:
            call_command('add_test_medical_direction')
            self.stdout.write(self.style.SUCCESS("Медицинские направления успешно добавлены"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении мед-направлений: {e}"))

        try:
            call_command('add_test_doctors')
            self.stdout.write(self.style.SUCCESS("Доктора успешно добавлены"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении докторов: {e}"))

        try:
            call_command('add_test_information')
            self.stdout.write(self.style.SUCCESS("Информация со страниц успешно добавлена"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении информации со страниц: {e}"))

        try:
            call_command('add_test_servises')
            self.stdout.write(self.style.SUCCESS("Услуги успешно добавлены"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении услуг: {e}"))

        try:
            call_command('add_test_appointment')
            self.stdout.write(self.style.SUCCESS("Записи на приём успешно добавлены"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении записей на приём: {e}"))

        try:
            call_command('add_test_diagnostic_results')
            self.stdout.write(self.style.SUCCESS("Результаты успешно добавлены"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении результатов анализов: {e}"))

        try:
            call_command('add_test_test_result')
            self.stdout.write(self.style.SUCCESS("Результаты тестов успешно добавлены"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при добавлении результатов тестов: {e}"))

        self.stdout.write(self.style.SUCCESS("Все тестовые данные успешно загружены!"))
