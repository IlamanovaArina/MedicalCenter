import os
from django.core.files import File
from django.core.management import BaseCommand
from medical.models import Information

class Command(BaseCommand):
    help = "Добавить или обновить тестовые данные в Information"

    def handle(self, *args, **kwargs):
        # Получаем или создаем "соло" объект
        info_obj = Information.get_solo()

        # Открываем файлы
        with open(os.path.join('static', 'images', 'doctors.webp'), 'rb') as f1, \
             open(os.path.join('static', 'images', 'hospital.avif'), 'rb') as f2:
            image_the_main_page = File(f1)
            image_from_the_company = File(f2)

            # Обновляем поля объекта
            info_obj.text_from_the_main_page = (
                'Добро пожаловать. В наших клиниках вас встретят специалисты своего дела, позаботятся о вашем '
                'здоровье и состоянии. Тут вы встретите современное, качественное оборудование, которое '
                'предоставляет высокоточные результаты анализов. На нашем сайте, на странице профиля вы найдёте'
                'ваши записи на приём, актуальные и завершённые. Когда будут готовы анализы, вы сможете их '
                'посмотреть перейдя по ссылки в карточки с записью на приём. Если найдёте какие-то недостатки на '
                'сайте или ошибки, можете связаться в форме обратной связи, вы её найдёте на главной странице. '
                'И дальше какой-то текст, что бы страница не была пустой. Спасибо что дочитали до этого момента.'
            )
            info_obj.company_history = (
                'Наша компания была основана много лет назад, мы работали над качеством предоставляемых услуг, '
                'закупали новое оборудование, благодаря спонсированию от благотворительных фондов: "..." и "...".'
                'В сложные периоды эпидемии мы переоборудовали не мало помещений, что бы предоставить места для '
                'госпитализированных. Ладно, тут в общем можно написать историю компании поподробнее.'
            )
            info_obj.mission = 'Совершенствоваться во всех параметрах'
            info_obj.purposes = 'Получить звание Лучшей клиники области.'
            info_obj.image_the_main_page = image_the_main_page
            info_obj.image_from_the_company = image_from_the_company
            info_obj.phone = '79333333333'
            info_obj.email = 'medical.center@gmail.com'
            info_obj.address = 'г. Адрес, ул. Клиники, д 173'

            # Сохраняем объект
            info_obj.save()

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены или обновлены!"))
