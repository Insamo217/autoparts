from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index_url'),
    path('category/', category),
    path('brands/', brands),
    path('category/<str:category>/', categories_list),
    path('category/<str:category>/<str:category_name>/', spares, name='category_url'),
    path('category/<str:category>/<str:category_name>/<str:id>/', spare_card),
    path('category/<str:category>/<str:category_name>/<str:id>/buy_card',
         buy_card, name='buy_url'),

    path('brands/KIA/', kia_card),
    path('brands/Skoda/', skoda_card),
    path('brands/Hyunday/', hyunday_card),
    path('brands/Volvo/', volvo_card),
    path('brands/Opel/', opel_card),
]
