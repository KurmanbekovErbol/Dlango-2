from django.urls import path
from main.views import mein

urlpatterns = [
    path('', mein, name='main'),
]
