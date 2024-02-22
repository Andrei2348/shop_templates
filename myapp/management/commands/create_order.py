from django.core.management.base import BaseCommand
from myapp.models import Client, Orders



class Command(BaseCommand):
    help = 'Создание пустого заказа для пользователя'

    def handle(self, *args, **kwargs):
        if kwargs['index']:
            index = kwargs['index']
            clients = Client.objects.all()
            try:
                order = Orders(
                    customer=clients[index-1],
                    amount=0
                )
                order.save()
                self.stdout.write('В Таблице созданы заказы')
            except IndexError:
                self.stdout.write('В таблице отсутствует пользователь с таким pk')
        else:
            self.stdout.write('Ошибка создания заказа.')


    def add_arguments(self, parser):
        parser.add_argument('index', type=int, help='Указывает id пользователя, который делает заказ')

        