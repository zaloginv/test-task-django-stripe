from payment_app.models import Item
from django.core.management.base import BaseCommand
from random import choice, randint


class Command(BaseCommand):
    def handle(self, **options):
        item_name_start_list = ['Смартфон', 'Пылесос', 'Игровой ноутбук', 'Лампочка']
        item_name_middle_list = ['Apple', 'LG', 'Tecno', 'Philips']
        item_name_end_list = ['3000', 'X9', 'Note 7i', '13', 'Super', 'Mega']

        item_description_list = ['Новинка на рынке технологий, новый дизайн, новая начинка, в три раза больше '
                                 'производительность',
                                 'Современное устройство, которое нужно в каждом доме, каждому ребенку, '
                                 'каждой домохозяйке, каждой собаке',
                                 'Лучший товар от лучшего продавца на свете! Покупайте, пока не кончилось!']

        for _ in range(20):
            Item(name=f'{choice(item_name_start_list)} {choice(item_name_middle_list)} {choice(item_name_end_list)}',
                 description=choice(item_description_list),
                 price=randint(100000,1000000) \
                .save()
