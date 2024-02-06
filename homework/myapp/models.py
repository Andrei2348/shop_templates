from django.db import models



class Client(models.Model):
    '''Модель клиента'''
    name = models.CharField(max_length=60, db_index=True)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    date_reg = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Products(models.Model):
    '''Модель товара'''
    title = models.CharField(max_length=60, db_index=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, upload_to="images")
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title


class Orders(models.Model):
    '''Модель заказа'''
    customer = models.ForeignKey('Client', 
                                on_delete=models.CASCADE,
                                related_name='customer', 
                                null='True')
    product = models.ManyToManyField('Products', related_name='product')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_reg = models.DateField(auto_now=True)

    def __str__(self):
        return f'Заказ клиента: {str(self.customer)}'
