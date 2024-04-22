from django.http import HttpResponse
from .food_models import *
from .food_data import *
from django.shortcuts import render
from .food_contants import *
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()
from GyeongJu.models import hard_coded_text

def foodIndex(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    if request.method == 'GET':
        korean_data = korean_food_model.objects.filter(lang = lang)
        western_data = western_food_model.objects.filter(lang = lang)
        japanese_data = japanese_food_model.objects.filter(lang = lang)
        chinese_data = chinese_food_model.objects.filter(lang = lang)
        food_form = text_food_form.objects.filter(lang = lang).first()
        return render(request, 'food/food_home.html', {'korean': korean_data, 'western': western_data, 
                                                       'japanese': japanese_data, 'chinese': chinese_data, 
                                                       'food_form': food_form, 'hard_coded': text_data})

def korean_food_view(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    if request.method == 'GET':
        korean_data = None
        korean_data = korean_food_model.objects.filter(lang=lang)
        food_form = text_food_form.objects.filter(lang = lang).first()
        return render(request, 'food/food_home.html', {'korean': korean_data, 'food_form': food_form, 'hard_coded': text_data})

def western_food_view(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    if request.method == 'GET':
        western_data = None
        western_data = korean_food_model.objects.filter(lang=lang)
        food_form = text_food_form.objects.filter(lang = lang).first()
        return render(request, 'food/food_home.html', {'western': western_data, 'food_form': food_form, 'hard_coded': text_data})

def japanese_food_view(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    if request.method == 'GET':
        japanese_data = None
        japanese_data = japanese_food_model.objects.filter(lang=lang)
        food_form = text_food_form.objects.filter(lang = lang).first()
        return render(request, 'food/food_home.html', {'japanese': japanese_data, 'food_form': food_form, 'hard_coded': text_data})

def chinese_food_view(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    if request.method == 'GET':
        chinese_data = None
        chinese_data = korean_food_model.objects.filter(lang=lang)
        food_form = text_food_form.objects.filter(lang = lang).first()
        return render(request, 'food/food_home.html', {'chinese': chinese_data, 'food_form': food_form, 'hard_coded': text_data})

