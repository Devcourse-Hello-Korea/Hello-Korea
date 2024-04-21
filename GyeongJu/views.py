from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'Home.html')

def gyeongju_index(request):
    return render(request, 'GyeongJu_Home.html')

def sooncheon_index(request):
    return render(request, 'Sooncheon_Home.html')

def jeonju_index(request):
    return render(request, 'Jeonju_Home.html')
