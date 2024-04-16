from django.http import HttpResponse
from .food_models import *
from .food_data import *
from django.shortcuts import render
from .food_contants import *

def food_index(request):
    if request.method == 'GET':
        korean_data, western_data, japanese_data, chinese_data = None, None, None, None
        korean_food_model.objects.all().delete()
        western_food_model.objects.all().delete()
        japanese_food_model.objects.all().delete()
        chinese_food_model.objects.all().delete()
        get_food_data(KOREAN_URL, 'korean', 11)
        get_food_data(WESTERN_URL, 'western', 4)
        get_food_data(JAPANESE_URL, 'japanese',2)
        get_food_data(CHINESE_URL, 'chinese',1)
        korean_data = korean_food_model.objects.all()
        western_data = western_food_model.objects.all()
        japanese_data = japanese_food_model.objects.all()
        chinese_data = chinese_food_model.objects.all()
        return render(request, 'food/index.html', {'korean': korean_data, 'western': western_data, 'japanese': japanese_data, 'chinese': chinese_data})

def korean_food_view(request):
    return HttpResponse("한식 페이지")

def western_food_view(request):
    return HttpResponse("양식 페이지")

def japanese_food_view(request):
    return HttpResponse("일식 페이지")

def chinese_food_view(request):
    return HttpResponse("중식 페이지")
