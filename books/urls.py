from django.urls import path
from .views import name_view
from .views import hobby_view
from .views import time_view


urlpatterns = [
    path('name/', name_view, name='hello'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', time_view, name='time'),
]