from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Home | Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)


def about(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'О нас',
        'content': 'Страница о нас',
    }

    return render(request, 'main/about.html', context)
