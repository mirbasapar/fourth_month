from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def name_view(request):
    if request.method == 'GET':
        return HttpResponse('Я, Сапаров Мирбек. Мне 35 лет.')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('Люблю путешествовать и отдых')


def time_view(request):
    if request.method == 'GET':
        now = datetime.now()
        return HttpResponse(f'Текущее время: {now}')
# Create your views here.
