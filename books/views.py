from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models, forms


def update_book_view(request, id):
    book_id = get_object_or_404(models.Books, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Book edited!</h3>')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='edit.html', context={'book_id': book_id, 'form': form})


def delete_book_view(request, id):

    print(request)
    book_id = get_object_or_404(models.Books, id=id)
    book_id.delete()

    return HttpResponse("ваша книга была удалена")


def create_review_view(request, id):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Your review has been added!</h1>')
    else:
        form = forms.ReviewForm()
    return render(request, template_name='create_review.html', context={'form': form})


def books_view(request):
    if request.method == 'GET':
        books = models.Books.objects.all().filter().order_by('-id')
        print(books)
        return render(request, template_name='books.html', context={'books': books})

def books_detail_view(request, id):
    if request.method == 'GET':
        books_id = get_object_or_404(models.Books, id=id)
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