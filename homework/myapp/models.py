from django.db import models



class Client(models.Model):
    '''Модель клиента'''
    name = models.CharField(max_length=60, db_index=True, verbose_name="Имя клиента")
    email = models.EmailField(max_length = 254, verbose_name="E-mail")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона")
    address = models.CharField(max_length=120, verbose_name="Адрес")
    date_reg = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Клиент магазина'
        verbose_name_plural = 'Клиенты магазина'
    
    
class Products(models.Model):
    '''Модель товара'''
    title = models.CharField(max_length=60, db_index=True, verbose_name="Название продукта")
    description = models.CharField(max_length=200, verbose_name="Описание продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена продукта")
    image = models.ImageField(blank=True, upload_to="images", verbose_name="Фото")
    quantity = models.IntegerField(verbose_name="Количество в наличии")
    date_add = models.DateField(auto_now_add=True, verbose_name="Дата добавления")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Orders(models.Model):
    '''Модель заказа'''
    customer = models.ForeignKey('Client', 
                                on_delete=models.CASCADE,
                                related_name='customer', 
                                null='True',
                                verbose_name="Покупатель")
    product = models.ManyToManyField('Products', related_name='product', verbose_name="Название продукта")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    date_reg = models.DateField(auto_now=True, verbose_name="Дата оформления")

    def __str__(self):
        return f'Заказ клиента: {str(self.customer)}'

    class Meta:
        verbose_name = 'Заказ Клиента'
        verbose_name_plural = 'Заказы клиента'

         
