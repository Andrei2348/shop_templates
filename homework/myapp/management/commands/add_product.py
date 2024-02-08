from django.core.management.base import BaseCommand
from myapp.models import Client, Products, Orders
from random import choice



class Command(BaseCommand):
    help = 'Добавление продуктов в заказ'

    def handle(self, *args, **kwargs):
        if kwargs['index']:
            index = kwargs['index']
            try:
                order = Orders.objects.get(customer=index)
                # Получаем список всех продуктов
                products = Products.objects.all()
                # Выбираем случайный товар и добавляем в заказ
                prod = choice(products)
                # Проверка существования товара в списке заказа
                if prod not in order.product.all():
                    order.product.add(prod)
                    # Изменяем стоимость заказа
                    Orders.objects.filter(customer=index).update(amount = (order.amount + prod.price))
                    self.stdout.write(f'Товар {prod} успешно добавлен в заказ.')
                else:
                    self.stdout.write(f'Товар {prod} уже есть в списке заказа.')
            except IndexError:
                self.stdout.write('В таблице отсутствует пользователь с таким pk.')
        else:
            self.stdout.write('Ошибка добавления товара в заказ.')


    def add_arguments(self, parser):
        parser.add_argument('index', type=int, help='Указывает id пользователя, который делает заказ')


