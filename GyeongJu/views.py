from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import *


def index(request):
    return HttpResponse('경주 페이지')
