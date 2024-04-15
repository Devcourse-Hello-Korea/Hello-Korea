from django.urls import path
from . import views
from .Accomodation import accomodation_views
from .KoreaTradition import tradition_views

urlpatterns = [
    # localhost:8000/GyeongJu
    path('', views.index, name='index'),
    path('Accomodation', accomodation_views.accomodation_view),
<<<<<<< HEAD
    path('Tradition', tradition_views.tradition_view),
=======
    path('food', views.food_index),
>>>>>>> main
]