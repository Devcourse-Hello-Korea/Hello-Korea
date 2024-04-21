from django.urls import path
from . import views
from .Souvenir import souvenir_views
from .Accomodation import accomodation_views
from .food import food_views
from .KoreaTradition import tradition_views

urlpatterns = [
    # localhost:8000/GyeongJu
    path('', views.index, name='index'),
    path('GyeongJu/', views.gyeongju_index, name='gyeongju_index'),
    path('SoonCheon/', views.sooncheon_index, name='sooncheon_index'),
    path('JeonJu/', views.jeonju_index, name='jeonju_index'),
    path('GyeongJu/Souvenir/', souvenir_views.Souvenir.as_view(), name='souvenir'),
    path('GyeongJu/Accomodation', accomodation_views.accomodation_view),
    path('GyeongJu/Food', food_views.foodIndex),
    path('GyeongJu/Food/korean', food_views.korean_food_view),
    path('GyeongJu/Food/western', food_views.western_food_view),
    path('GyeongJu/Food/japanese', food_views.japanese_food_view),
    path('GyeongJu/Food/chinese', food_views.chinese_food_view),
    path('GyeongJu/Tradition', tradition_views.tradition_view),
    path('GyeongJu/Tradition/clothes', tradition_views.clothes_view),
    path('GyeongJu/Tradition/accomodation', tradition_views.accomodation_view),
]
