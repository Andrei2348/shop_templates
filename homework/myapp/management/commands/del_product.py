from django.core.management.base import BaseCommand
from myapp.models import Client, Products, Orders
from random import choice



class Command(BaseCommand):
    help = 'Удаление продуктов из заказа'

    def handle(self, *args, **kwargs):
        index_client = kwargs['index1']
        index_product = kwargs['index2']
        if kwargs['index1'] and kwargs['index2']:
            try:
                order = Orders.objects.get(customer=index_client)
                prod = Products.objects.get(pk=index_product)
                # Проверка существования товара в списке заказа
                if prod in order.product.all():
                    order.product.remove(prod)
                    # Изменяем стоимость заказа
                    Orders.objects.filter(customer=index_client).update(amount = (order.amount - prod.price))
                    self.stdout.write(f'Товар {prod} успешно удален из заказа.')
                else:
                    self.stdout.write(f'Товар {prod} отсутствует в списке заказа.')
            except IndexError:
                self.stdout.write('В таблице отсутствует такие pk.')
        else:
            self.stdout.write('Ошибка удаления товара из заказа.')


    def add_arguments(self, parser):
        parser.add_argument('index1', type=int, help='Указывает id пользователя, который делает заказ')
        parser.add_argument('index2', type=int, help='Указывает id пользователя, который делает заказ')


