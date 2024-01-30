from django.db import models



class Client(models.Model):
    '''Модель клиента'''
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    date_reg = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Products(models.Model):
    '''Модель товара'''
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Orders(models.Model):
    '''Модель заказа'''
    customer = models.ForeignKey('Client', 
                                on_delete=models.CASCADE,
                                related_name='username', 
                                null='True', 
                                verbose_name='Id клиента')
    product = models.ManyToManyField('Products',
                                related_name='product_title',
                                verbose_name='Id товара')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_reg = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.product

    # def save(self, *args, **kwargs):

    #     super().save(*args, **kwargs)