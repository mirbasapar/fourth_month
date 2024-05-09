from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import PostBooks


def post_books_view(request):
    if request.method == 'GET':
        posts = PostBooks.objects.filter().order_by('-id')
        return render(request, template_name='post.html',
                      context={'posts': posts})

def post_books_detail_view(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(PostBooks, id=id)
        return render(request, template_name='post_detail.html',
                      context={'post_id': post_id})


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
