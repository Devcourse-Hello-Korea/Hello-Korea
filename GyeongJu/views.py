from django.http import HttpResponse

def index(request):
    return HttpResponse('경주 페이지')
