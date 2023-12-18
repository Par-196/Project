from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def main_page(request):
    items = Product.objects.all()
    lists = {
        "items": items
    }
    return render(request, "main_page.html", lists)


def goods(request, my_id):
    item = Product.objects.get(id=my_id)
    lists = {
        "item": item
    }
    return render(request, "goods.html", lists)
