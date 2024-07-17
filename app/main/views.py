from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Home',
        'content': 'Home page',
    }

    return render(request, 'main/index.html', context)


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('About page')
