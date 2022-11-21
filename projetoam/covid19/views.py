from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    test_function()

    return render(request, 'index.html')


def test_function():
    a = 10
    a = a + 1
    return True