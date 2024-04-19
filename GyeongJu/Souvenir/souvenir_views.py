from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .souvenir_models import Bread, Shop, ShopLocation

#차후 언어 변경시 수정 필요
test_lang = 'en' #['ko', 'en', 'ja', 'zh-cn', 'zh-tw', 'de', 'ru']

class Souvenir(View):
    def get(self, request):
        breads = Bread.objects.filter(lang=test_lang)[:6]
        shops = Shop.objects.filter(lang=test_lang)[:7]
        shop_locations = ShopLocation.objects.filter()[:7]

        context = {
            'breads': breads,
            'shops': shops,
            'shop_locations': shop_locations,
        }

        return render(
            request,
            'souvenir/souvenir.html',
            context
        )