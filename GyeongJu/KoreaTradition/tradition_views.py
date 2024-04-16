from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from .models import TraditionExperienceInfo
from .crawl import *

def tradition_view(request):
    GyeongJuCrawler()
    data = TraditionExperienceInfo.objects.all().distinct()
    return render(request, 'GyeongJu/tradition/index.html', {'data': data})
