from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from myapp.models import Products
from random import randint


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(0, 5):
            products = Products(
                title=f'Продукт № {i}',
                description=lorem_ipsum.paragraphs(4)[0],
                price=i + 4.5,
                quantity=randint(1, 15)
            )
            products.save()
        self.stdout.write(f'В Таблице созданы 5 товаров')
            
        
        
     