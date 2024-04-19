from django.shortcuts import render, redirect
from .models import *
from .experience_constant import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def tradition_view(request):
    typename = TypeInfo.objects.get(type='전통문화체험')
    if request.method == 'POST':
        cur_lang = request.POST['select_language']
        LanguageInfo.objects.filter(selected=True).update(selected=False)
        LanguageInfo.objects.filter(lang=cur_lang).update(selected=True)
        language = LanguageInfo.objects.all()
        data = TraditionExperienceInfo.GetInfoByTypeLang(type_name=typename, language=cur_lang)
        return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename, 'language': language})
    else:
        get_lang = LanguageInfo.GetCurrentLanguage()
        language = LanguageInfo.objects.all()
        data = TraditionExperienceInfo.GetInfoByTypeLang(type_name=typename, language=get_lang.lang)
        return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename, 'language': language})

@csrf_exempt
def clothes_view(request):
    typename = TypeInfo.objects.get(type='의복체험')
    if request.method == 'POST':
        cur_lang = request.POST['select_language']
        LanguageInfo.objects.filter(selected=True).update(selected=False)
        LanguageInfo.objects.filter(lang=cur_lang).update(selected=True)
        language = LanguageInfo.objects.all()
        data = TraditionExperienceInfo.GetInfoByTypeLang(type_name=typename, language=cur_lang)
        return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename, 'language': language})
    else:
        get_lang = LanguageInfo.GetCurrentLanguage()
        print(get_lang)
        language = LanguageInfo.objects.all()
        print(language)
        data = TraditionExperienceInfo.GetInfoByTypeLang(type_name=typename, language=get_lang.lang)
        return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename, 'language': language})

@csrf_exempt
def accomodation_view(request):
    typename = TypeInfo.objects.get(type='고택체험')
    if request.method == 'POST':
        cur_lang = request.POST['select_language']
        LanguageInfo.objects.filter(selected=True).update(selected=False)
        LanguageInfo.objects.filter(lang=cur_lang).update(selected=True)
        language = LanguageInfo.objects.all()
        data = TraditionExperienceInfo.GetInfoByTypeLang(type_name=typename, language=cur_lang)
        return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename, 'language': language})
    else:
        get_lang = LanguageInfo.GetCurrentLanguage()
        language = LanguageInfo.objects.all()
        data = TraditionExperienceInfo.GetInfoByTypeLang(type_name=typename, language=get_lang.lang)
        return render(request, 'GyeongJu/tradition/index.html', {'data': data, 'type': typename, 'language': language})
