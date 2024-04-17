from django.shortcuts import render
from .models import TraditionExperienceInfo, TypeInfo
from .experience_constant import *

def tradition_view(request):
    typename = TypeInfo.objects.get(type='전통문화체험')
    data = TraditionExperienceInfo.GetInfoByType(type_name=typename)
    return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename})

def clothes_view(request):
    typename = TypeInfo.objects.get(type='의복체험')
    data = TraditionExperienceInfo.GetInfoByType(type_name=typename)
    return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename})

def accomodation_view(request):
    typename = TypeInfo.objects.get(type='고택체험')
    data = TraditionExperienceInfo.GetInfoByType(type_name=typename)
    return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename})
