from django.shortcuts import render
from .models import *


def index(request):
    title = 'Start'
    return render(request, 'spares/index.html', context={'title': title})


def category(request):
    categories_list = \
        ['Двигатель', 'Колесные диски', 'Кузов внутри', 'Пневматическая система',
         'Подвеска', 'Рулевое управление', 'Кондиционирование',
         'Система охлаждения', 'Трансмиссия', 'Электроосвещение', 'Тормозная система']
    return render(request, 'spares/category.html',
                  context={'categories_list': categories_list})


def categories_list (request, category):
    if category=='Тормозная система':
        categories_list = Category.objects.filter \
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category=='Двигатель':
        categories_list = Category.objects.filter \
            (id__in=[10,12,13,14,16,18,21,25,32,
                     58,67,68,69,70,73,75,80,87,91,94,114,127,133])
    elif category == 'Колесные диски':
        categories_list = Category.objects.filter\
            (id__in=[18,35,38,78])
    elif category == 'Кузов внутри':
        categories_list = Category.objects.filter\
            (id__in=[5,10,16,18,28,54,103,125,126,127,129,130])
    elif category == 'Пневматическая система':
        categories_list = Category.objects.filter\
            (id__in=[32,39,40,48])
    elif category == 'Подвеска':
        categories_list = Category.objects.filter\
            (id__in=[3,10,16,18,54,55,64,70,80,91,
                     104,105,119,126])
    elif category == 'Рулевое управление':
        categories_list = Category.objects.filter\
            (id__in=[5,10,12,16,18,54,64,80,91,106,
                     126,139])
    elif category == 'Кондиционирование':
        categories_list = Category.objects.filter \
        (id__in=[42,48,80,106,139])
    elif category == 'Система охлаждения':
        categories_list = Category.objects.filter\
            (id__in=[9,16,54,55,66,75,84,85,87,122,130,
                     133,140])
    elif category == 'Трансмиссия':
        categories_list = Category.objects.filter\
            (id__in=[5,12,16,18,22,23,25,26,28,54,55,62,63,64,
                     66,80,81,87,89,91,95,104,105,106,129,130,142])
    elif category == 'Электроосвещение':
        categories_list = Category.objects.filter\
            (id__in=[6,7,9,15,16,17,19,22,30,31,32,49,55,66,
                     74,83,86,95,97,111,112,118,143])

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


def buy_card(request, category_name, id, category):
    return render(request, 'spares/buy_card.html')


def brands(request):
    brands = Brand.objects.all()
    return render(request, 'spares/brands.html',
                  context={'brands': brands})


def kia_card(request):
    brand = Brand.objects.filter(name='KIA')
    return render(request, 'spares/brands/kia_card.html',
                  context={'brand': brand, 'spares': spares})


def skoda_card(request):
    brand = Brand.objects.filter(name='Skoda')
    return render(request, 'spares/brands/skoda_card.html',
                  context={'brand': brand, 'spares': spares})


def volvo_card(request):
    brand = Brand.objects.filter(name='Volvo')

    return render(request, 'spares/brands/volvo_card.html',
                  context={'brand': brand, 'spares': spares})


def hyunday_card(request):
    brand = Brand.objects.filter(name='Hyunday')

    return render(request, 'spares/brands/hyunday_card.html',
                  context={'brand': brand, 'spares': spares})


def opel_card(request):
    brand = Brand.objects.filter(name='Opel')
    return render(request, 'spares/brands/opel_card.html',
                  context={'brand': brand, 'spares': spares})









