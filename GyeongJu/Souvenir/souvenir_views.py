from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .souvenir_models import Bread, Shop, ShopLocation, text_souvenir_form

class Souvenir(View):
    def get(self, request):
        lang = request.COOKIES.get('user_lang', 'ko')
        breads = Bread.objects.filter(lang=lang)[:6]
        shops = Shop.objects.filter(lang=lang)[:7]
        shop_locations = ShopLocation.objects.filter()[:7]
        form_text = text_souvenir_form.objects.filter(lang=lang).first()

        context = {
            'breads': breads,
            'shops': shops,
            'shop_locations': shop_locations,
            'shop': form_text.shop, 
            'bread': form_text.bread
        }


        return render(
            request,
            'souvenir/souvenir.html',
            context,
        )