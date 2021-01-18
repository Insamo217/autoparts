from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index_url'),
    path('category/', category),
    path('category/<str:category>/', categories_list),
    path('category/<str:category>/<str:category_name>/', spares, name='category_url'),
    path('category/<str:category>/<str:category_name>/<str:id>/', spare_card),

]
