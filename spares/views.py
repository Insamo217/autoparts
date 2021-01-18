from django.shortcuts import render
from .models import *


def index(request):
    title = 'Start'
    return render(request, 'spares/index.html', context={'title': title})


def category(request):
    categories_list = ['Передняя подвеска', 'Тормозная система', 'Three']
    return render(request, 'spares/category.html',
                  context={'categories_list': categories_list})


def spares(request, category_name, category):
    search_query = request.GET.get('search', '')
    title = category_name
    if search_query:
        spares = Spares.objects.filter(number__icontains=search_query)
    else:
        spares = Spares.objects.filter(category_name=category_name)

    return render(request, 'spares/spares.html',
                  context={'spares': spares, 'title': title})


def spare_card(request, category_name, id, category):
    spares = Spares.objects.filter(id=id)
    return render(request, 'spares/spare_card.html',
                  context={'spares': spares})


def categories_list (request, category):
    if category=='Передняя подвеска':
        categories_list = Category.objects.filter\
            (id__in=[3,10,16,18,66,91,104,105,106,120,141])
    elif category=='Тормозная система':
        categories_list = Category.objects.filter \
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    return render(request, 'spares/category.html',
                  context={'categories_list': categories_list})






