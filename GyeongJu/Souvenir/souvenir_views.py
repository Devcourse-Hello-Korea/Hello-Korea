from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .souvenir_models import Breads


class Souvenir(View):
    def get(self, request):
        breads = Breads.objects.all()

        context = {
            'breads': breads,
        }

        return render(
            request,
            'souvenir/souvenir.html',
            context
        )