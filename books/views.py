from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Books


def books_view(request):
    if request.method == 'GET':
        books = Books.objects.filter().order_by('-id')
        return render(request, template_name='books.html', context={'books': books})

def books_detail_view(request, id):
    if request.method == 'GET':
        books_id = get_object_or_404(Books, id=id)
        return render(request, template_name='books_detail.html', context={'books_id': books_id})


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
