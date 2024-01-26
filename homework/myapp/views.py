from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    html = '<h1>Привет</h1><br><h3>Меня зовут Андрей</h3><p>Я учусь на Python-разработчика</p>'
    return HttpResponse(html)


def about(request):
    html = '<h1>Привет</h1><br><p>"Это мой уже не первый сайт на django"</p>'
    return HttpResponse(html)