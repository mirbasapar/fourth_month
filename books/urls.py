from django.urls import path
from .views import name_view
from .views import hobby_view
from .views import time_view
from .views import post_books_view, post_books_detail_view


urlpatterns = [
    path('name/', name_view, name='hello'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', time_view, name='time'),
    path('books/', post_books_view, name='books'),
    path('books/<int:id>/', post_books_detail_view, name='books_detail'),
]