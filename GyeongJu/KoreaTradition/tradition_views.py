from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from .models import TraditionExperienceInfo
from .experience_constant import *
from .crawl import *

def tradition_view(request):
    GyeongJuCrawler(EXPERIENCE_URL)
    typename = TypeInfo.objects.get(type='전통문화체험')
    data = TraditionExperienceInfo.GetInfoByType(type_name=typename)
    return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename})

def clothes_view(request):
    GyeongJuCrawler(CLOTHES_URL)
    typename = TypeInfo.objects.get(type='의복체험')
    data = TraditionExperienceInfo.GetInfoByType(type_name=typename)
    return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename})

def accomodation_view(request):
    GyeongJuCrawler(TRADITIONAL_ACCOMODATION_URL)
    typename = TypeInfo.objects.get(type='고택체험')
    data = TraditionExperienceInfo.GetInfoByType(type_name=typename)
    return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename})
