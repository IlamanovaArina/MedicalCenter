from django.core.management import BaseCommand

from medical.models import MedicalDirection


class Command(BaseCommand):
    help = "Добавляет данные medical_direction"

    def handle(self, *args, **kwargs):
        # Пример добавления одного объекта

        my_instance_1 = MedicalDirection(
            name='Неврология',
            description='Изучение нервной системы, её функций и заболеваний. '
                        'Основано на диагностировании и лечении нарушений в работе '
                        'головного, спинного мозга, нервной системы.',
        )
        my_instance_1.save()

        my_instance_2 = MedicalDirection(
            name='Эндокринология',
            description='Диагностика и терапия гормональных нарушений, '
                        'таких как диабет, заболевания щитовидной железы и '
                        'другие.',
        )
        my_instance_2.save()

        my_instance_3 = MedicalDirection(
            name='Иммунология',
            description='Изучение иммунитета, его основных функций и '
                        'возможных нарушений (иммунодефицит, аутоиммунные '
                        'нарушения, аллергические реакции).',
        )
        my_instance_3.save()

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))