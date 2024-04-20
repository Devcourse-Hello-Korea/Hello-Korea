from django.http import HttpResponse
from .food_models import *
from .food_data import *
from django.shortcuts import render
from .food_contants import *

#차후 언어 변경시 수정 필요
test_lang = 'en' #['ko', 'en', 'ja', 'zh-cn', 'zh-tw', 'de', 'ru']

def food_index(request):
    if request.method == 'GET':
        korean_data = korean_food_model.objects.filter(lang = test_lang)
        western_data = western_food_model.objects.filter(lang = test_lang)
        japanese_data = japanese_food_model.objects.filter(lang = test_lang)
        chinese_data = chinese_food_model.objects.filter(lang = test_lang)
        return render(request, 'food/food_home.html', {'korean': korean_data, 'western': western_data, 'japanese': japanese_data, 'chinese': chinese_data})

def korean_food_view(request):
    if request.method == 'GET':
        korean_data = None
        korean_data = korean_food_model.objects.filter(lang=test_lang)
        return render(request, 'food/food_home.html', {'korean': korean_data})

def western_food_view(request):
    if request.method == 'GET':
        western_data = None
        western_data = korean_food_model.objects.filter(lang=test_lang)
        return render(request, 'food/food_home.html', {'western': western_data})

def japanese_food_view(request):
    if request.method == 'GET':
        japanese_data = None
        japanese_data = japanese_food_model.objects.filter(lang=test_lang)
        return render(request, 'food/food_home.html', {'japanese': japanese_data})

def chinese_food_view(request):
    if request.method == 'GET':
        chinese_data = None
        chinese_data = korean_food_model.objects.filter(lang=test_lang)
        return render(request, 'food/food_home.html', {'chinese': chinese_data})

