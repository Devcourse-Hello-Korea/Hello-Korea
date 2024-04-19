from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .souvenir_models import Bread, Shop, ShopLocation


class Souvenir(View):
    def get(self, request):
        breads = Bread.objects.filter()[:6]
        shops = Shop.objects.all()
        shop_locations = ShopLocation.objects.all()

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