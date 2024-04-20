# from django.shortcuts import render
# import logging
# from django.http import HttpResponse
#
# logger = logging.getLogger(__name__)
#
#
# def index(request):
#     logger.info('Index page accessed')
#     return HttpResponse("Hello, world!")
#
#
# def about(request):
#     try:
#
#         result = 1 / 0
#     except Exception as e:
#         logger.exception(f'Error in about page: {e}')
#         return HttpResponse("Oops, something went wrong.")
#     else:
#         logger.debug('About page accessed')
#         return HttpResponse("This is the about page.")

# Create your views here.

import logging

from django.http import HttpResponse

# Получаем экземпляр логгера
logger = logging.getLogger(__name__)


def index(request):
    logger.info(f"Посетитель зашёл на главную страницу: {request.user}")
    return HttpResponse("<h1>Добро пожаловать на страницу Иванова Ивана Иваныча</h1>"
                        "<p>Описание главной страницы...</p>")


def about(request):
    logger.info(f"Посетитель посетил страницу 'О себе': {request.user}")
    return HttpResponse("<h1>О сайте</h1>"
                        "<p>Информация о сайте Иванова Ивана Иваныча...</p>")
