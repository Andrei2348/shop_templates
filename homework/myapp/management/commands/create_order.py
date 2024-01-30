from django.core.management.base import BaseCommand
from myapp.models import Client, Products, Orders
from random import choice

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Products.objects.all()
        print(products)
        for i in range(0, 20):
            orders = Orders(
                customer=choice(clients),
                product.add(choice(products)),
                amount=0
            )
            
            orders.save()
        self.stdout.write(f'В Таблице созданы заказы')