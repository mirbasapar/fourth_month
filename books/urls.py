from django.urls import path
from .views import name_view
from .views import hobby_view
from .views import time_view
from .views import books_view, books_detail_view


urlpatterns = [
    path('name/', name_view, name='hello'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', time_view, name='time'),
    path('books/', books_view, name='books'),
    path('books/<int:id>/', books_detail_view, name='books_detail'),
]