"""
URL configuration for Hello_Korea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import os, django
from django.http import HttpResponseRedirect

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()
from GyeongJu.KoreaTradition.models import LanguageInfo

def set_language(request):
    user_language = request.GET.get('lang_c', 'ko')
    referer_url = request.META.get('HTTP_REFERER', '/GyeongJu')
    response = HttpResponseRedirect(referer_url)
    response.set_cookie('user_lang', user_language)
    LanguageInfo.objects.filter(selected=True).update(selected=False)
    LanguageInfo.objects.filter(lang=user_language).update(selected=True)
    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GyeongJu.urls')),
    path('set_language/', set_language, name='set_language'),
]
