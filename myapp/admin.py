from django.contrib import admin
from .models import Client, Products, Orders
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'date_reg')
    list_display_links = ('name',)
    fields = ['name', 'email', 'phone', 'address']
    ordering = ['date_reg', 'name']
    list_per_page = 10
    search_fields = ['name', 'address', 'phone', 'email']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'date_add')
    list_display_links = ('title',)
    fields = ['title', 'price', 'quantity', 'image']
    ordering = ['date_add', 'title']
    list_per_page = 10
    search_fields = ['title']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('customer', 'amount')
    list_display_links = ('customer',)
    fields = ['customer', 'product', 'amount']
    ordering = ['date_reg']
    list_per_page = 10
    search_fields = ['customer']