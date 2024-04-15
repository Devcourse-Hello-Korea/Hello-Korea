from django.urls import path
from . import views
from .Souvenir import souvenir_views
from .Accomodation import accomodation_views

urlpatterns = [
    # localhost:8000/GyeongJu
    path('', views.index, name='index'),
    path('souvenir/', souvenir_views.Souvenir.as_view(), name='souvenir'),
    path('Accomodation', accomodation_views.accomodation_view),
]