from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    return render(request, 'Home.html', {'hard_coded': text_data})

def gyeongju_index(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    return render(request, 'GyeongJu_Home.html', {'hard_coded': text_data})

def sooncheon_index(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    return render(request, 'Sooncheon_Home.html', {'hard_coded': text_data})

def jeonju_index(request):
    lang = request.COOKIES.get('user_lang', 'ko')
    text_data=hard_coded_text.objects.filter(lang = lang).first()
    return render(request, 'Jeonju_Home.html', {'hard_coded': text_data})
