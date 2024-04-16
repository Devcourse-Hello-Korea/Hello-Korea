from django.urls import path
from . import views
from .Accomodation import accomodation_views
<<<<<<< HEAD
from .food import food_views
=======
from .KoreaTradition import tradition_views
>>>>>>> main

urlpatterns = [
    # localhost:8000/GyeongJu
    path('', views.index, name='index'),
    path('Accomodation', accomodation_views.accomodation_view),
<<<<<<< HEAD
    path('food', food_views.food_index),
    path('food/korean', food_views.korean_food_view),
    path('food/western', food_views.western_food_view),
    path('food/japanese', food_views.japanese_food_view),
    path('food/chinese', food_views.chinese_food_view),
=======
    path('Tradition', tradition_views.tradition_view),
    path('food', views.food_index),
>>>>>>> main
]