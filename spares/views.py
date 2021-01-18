from django.shortcuts import render
from .models import *


def index(request):
    title = 'Start'
    return render(request, 'spares/index.html', context={'title': title})


def category(request):
    categories_list = \
        ['Двигатель', 'Инструмент', 'Колесные диски', 'Кузов', 'Масла',
         'Оптика', 'Пневматическая система', 'Подвеска', 'Рулевое управление',
         'Система охлаждения', 'Сопутствующие товары',
         'Трансмиссия', 'Электроосвещение', 'Передняя подвеска', 'Тормозная система']
    return render(request, 'spares/category.html',
                  context={'categories_list': categories_list})


def categories_list (request, category):
    if category=='Передняя подвеска':
        categories_list = Category.objects.filter\
            (id__in=[3,10,16,18,66,91,104,105,106,120,141])
    elif category=='Тормозная система':
        categories_list = Category.objects.filter \
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category=='Двигатель':
        categories_list = Category.objects.filter \
            (id__in=[10,12,13,14,16,18,21,25,32,
                     58,67,68,69,70,73,75,80,87,91,94,114,127,133])
    elif category == 'Инструмент':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Колесные диски':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Кузов':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Масла':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Оптика':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Пневматическая система':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Подвеска':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Рулевое управление':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Система охлаждения':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Сопутствующие товары':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Трансмиссия':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
    elif category == 'Электроосвещение':
        categories_list = Category.objects.filter\
            (id__in=[4, 10, 12, 16, 24, 106, 124])
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









