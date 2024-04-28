from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .souvenir_models import Bread, Shop, ShopLocation, text_souvenir_form
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()
from GyeongJu.models import hard_coded_text

class Souvenir(View):
    def get(self, request):
        lang = request.COOKIES.get('user_lang', 'ko')
        text_data=hard_coded_text.objects.filter(lang = lang).first()
        breads = Bread.objects.filter(lang=lang)[:6]
        shops = Shop.objects.filter(lang=lang)[:7]
        shop_locations = ShopLocation.objects.filter()[:7]
        form_text = text_souvenir_form.objects.filter(lang=lang).first()

        context = {
            'breads': breads,
            'shops': shops,
            'shop_locations': shop_locations,
            'shop': form_text.shop, 
            'bread': form_text.bread,
            'hard_coded': text_data,
        }


        return render(
            request,
            'souvenir/souvenir.html',
            context,
        )