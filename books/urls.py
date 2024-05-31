from django.urls import path
from .views import name_view
from .views import hobby_view
from .views import time_view

# from .views import books_view, books_detail_view
from . import views


urlpatterns = [
    path("name/", name_view, name="hello"),
    path("hobby/", hobby_view, name="hobby"),
    path("time/", time_view, name="time"),
    path("books/", views.BooksView.as_view(), name="books"),
    path("books/<int:id>/", views.BookDetailView.as_view(), name="books_detail"),
    path("books/<int:id>/delete/", views.DeleteBookView.as_view(), name="delete_books"),
    path("books/<int:id>/update/", views.UpdateBookView.as_view(), name="update_books"),
    path(
        "books/<int:id>/create_review/",
        views.CreateReviewView.as_view(),
        name="create_review",
    ),
    path("search/", views.SearchBookView.as_view(), name="search"),
]
