from django.shortcuts import render
from .models import Orders, Products
from datetime import date, timedelta
from forms import ProductCreateForm


def create_result(order):
    order_list = []
    username = order[0].customer
    for i in range(len(order)):
        order_list.append(tuple(order[i].product.all()))
    return order_list, username


def cart(request, index):
    order = Orders.objects.filter(customer = index)
    order_list, username = create_result(order)
    context = {
    'title': 'Все заказы',
    'username': username,
    'orders': order_list
    }
    
    return render(request, 'myapp/index.html', context=context)


def cart_week(request, index):
    today = date.today()
    delta = today - timedelta(days=7)
    order = Orders.objects.filter(customer = index, date_reg__gte=delta)
    order_list, username = create_result(order)
    context = {
    'title': 'Все заказы за неделю',
    'username': username,
    'orders': order_list
    }
    return render(request, 'myapp/index.html', context=context)


def cart_mounth(request, index):
    today = date.today()
    delta = today - timedelta(days=30)
    order = Orders.objects.filter(customer = index, date_reg__gte=delta)
    order_list, username = create_result(order)
    context = {
    'title': 'Все заказы за месяц',
    'username': username,
    'orders': order_list
    }
    return render(request, 'myapp/index.html', context=context)


def cart_year(request, index):
    today = date.today()
    delta = today - timedelta(days=365)
    order = Orders.objects.filter(customer = index, date_reg__gte=delta)
    order_list, username = create_result(order)
    context = {
    'title': 'Все заказы за год',
    'username': username,
    'orders': order_list
    }
    return render(request, 'myapp/index.html', context=context)


def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
        
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']


            product = Products(title=title, description=description, price=price, quantity=quantity)
            product.save()
            message = 'Продукт сохранен в БД'
        else:
            form = ProductCreateForm()
            message = 'Заполните форму'
            return render(request, 'myapp4/edit.html', {'form':
    form, 'message': message})