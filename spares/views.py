from django.shortcuts import render
from .models import *


def index(request):
    title = 'Start'
    return render(request, 'spares/index.html', context={'title': title})


def category(request):
    categories_list = Category.objects.all()
    return render(request, 'spares/category.html',
                  context={'categories_list': categories_list})


def spares(request, category_name):
    search_query = request.GET.get('search', '')
    title = category_name
    if search_query:
        spares = Spares.objects.filter(number__icontains=search_query)
    else:
        spares = Spares.objects.filter(category_name=category_name)

    return render(request, 'spares/spares.html',
                  context={'spares': spares, 'title': title})


def spare_card(request, category_name, id):
    spares = Spares.objects.filter(id=id)
    return render(request, 'spares/spare_card.html',
                  context={'spares': spares})




