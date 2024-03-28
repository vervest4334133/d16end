from django.urls import path

from word.cnt.views import word_list

urlpatterns = [
    path('index/', word_list, name='index'),
]
