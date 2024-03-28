from django.http import HttpResponse
from django.shortcuts import render

from word.cnt.models import Word


def word_list(request):
    words = Word.objects.all()

    return render(request, 'index.html',
                  {'words': words})
