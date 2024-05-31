from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views import generic
from . import models, forms


class SearchBookView(generic.ListView):
    template_name = "books.html"
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["q"] = self.request.GET.get("q")
        return contex


class BooksView(generic.ListView):
    template_name = "books.html"
    context_object_name = "books"
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


# def books_view(request):
#     if request.method == 'GET':
#         books = models.Books.objects.all().filter().order_by('-id')
#         print(books)
#         return render(request, template_name='books.html', context={'books': books})


class BookDetailView(generic.DetailView):
    template_name = "books_detail.html"
    context_object_name = "books_id"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=books_id)


# def books_detail_view(request, id):
#     if request.method == 'GET':
#         books_id = get_object_or_404(models.Books, id=id)
#         return render(request, template_name='books_detail.html', context={'books_id': books_id})


class UpdateBookView(generic.UpdateView):
    template_name = "edit.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=books_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBookView, self).form_valid(form=form)


# def update_book_view(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Book edited!</h3>')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, template_name='edit.html', context={'book_id': book_id, 'form': form})


class DeleteBookView(generic.DetailView):
    template_name = "confirm_delete.html"
    success_url = "books"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=books_id)


# def delete_book_view(request, id):
#     print(request)
#     book_id = get_object_or_404(models.Books, id=id)
#     book_id.delete()
#     return HttpResponse("ваша книга была удалена")


class CreateReviewView(generic.CreateView):
    template_name = "create_review.html"
    form_class = forms.ReviewForm
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)


# def create_review_view(request, id):
#     if request.method == 'POST':
#         form = forms.ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Your review has been added!</h1>')
#     else:
#         form = forms.ReviewForm()
#     return render(request, template_name='create_review.html', context={'form': form})


def name_view(request):
    if request.method == "GET":
        return HttpResponse("Я, Сапаров Мирбек. Мне 35 лет.")


def hobby_view(request):
    if request.method == "GET":
        return HttpResponse("Люблю путешествовать и отдых")


def time_view(request):
    if request.method == "GET":
        now = datetime.now()
        return HttpResponse(f"Текущее время: {now}")


# Create your views here.
