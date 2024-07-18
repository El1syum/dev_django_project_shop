from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        'title': 'Каталог',
        'goods': goods
    }

    return render(request, 'goods/catalog.html', context)


def product(request, slug):
    curr_product = Products.objects.get(slug=slug)

    context = {
        'product': curr_product
    }

    return render(request, 'goods/product.html', context)
