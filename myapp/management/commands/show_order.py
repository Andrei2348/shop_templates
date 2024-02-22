from django.core.management.base import BaseCommand
from myapp.models import Client, Orders



class Command(BaseCommand):
    help = 'Отображение содержимого заказа для пользователя'

    def handle(self, *args, **kwargs):
        if kwargs['index']:
            index = kwargs['index']
            clients = Client.objects.all()
            try:
                order = Orders.objects.get(customer=index)
                print(*order.product.all())
            except IndexError:
                self.stdout.write('В таблице отсутствует пользователь с таким pk')
        else:
            self.stdout.write('Ошибка отображения заказа.')


    def add_arguments(self, parser):
        parser.add_argument('index', type=int, help='Указывает id пользователя, который делает заказ')

        