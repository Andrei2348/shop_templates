from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from myapp.models import Client


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        for i in range(0, 5):
            client = Client(name=f'User_{i+1}',
                            email=f'user-{i}@example.com',
                            phone=f'+373333333{i}',
                            address=lorem_ipsum.paragraphs(3)[0]
            )
            self.stdout.write(f'Создан клиент {client}')
            client.save()
        
            
            
