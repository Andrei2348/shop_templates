from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = '<h1>Привет</h1><br><h3>Меня зовут Андрей</h3><p>Я учусь на Python-разработчика</p>'
    logger.info('Пользователь открыл страницу Index')
    return HttpResponse(html)


def about(request):
    html = '<h1>Привет</h1><br><p>"Это мой уже не первый сайт на django"</p>'
    logger.info('Пользователь открыл страницу About')
    return HttpResponse(html)