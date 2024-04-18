from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .souvenir_models import Bread, Shop


class Souvenir(View):
    def get(self, request):
        breads = Bread.objects.filter(pk__range=(1, 6))
        shops = Shop.objects.filter(pk__range=(1,7))

        context = {
            'breads': breads,
            'shops': shops
        }

        return render(
            request,
            'souvenir/souvenir.html',
            context
        )