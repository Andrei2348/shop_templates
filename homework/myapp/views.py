from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Orders




def cart(request, index):
    order = Orders.objects.filter(customer = index)
    order_list = []
    amount_list = []
    for i in range(len(order)):
        amount_list.append((order[i].amount))
        order_list.append(list(order[i].product.all()))
    context = {
    'title': 'Корзина товаров',
    'orders': order_list,
    'amount': amount_list
    }
    return render(request, 'myapp/index.html', context=context)