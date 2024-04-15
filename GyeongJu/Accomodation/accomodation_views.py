from django.shortcuts import render
from .accomodation_models import AccomodationInfo
from .accomodation_forms import CheckinCheckoutForm
from .accomodation_crawl import set_dates_and_crawl

def accomodation_view(request):
    data = None
    gyeongJu_Accomodation_Url = "https://www.google.com/travel/search?q=%EA%B2%BD%EC%A3%BC%20%EC%88%99%EC%86%8C&g2lb=2503771%2C2503781%2C4284970%2C4291517%2C4814050%2C4874190%2C4893075%2C4965990%2C72277293%2C72302247%2C72317059%2C72406588%2C72414906%2C72421566%2C72458066%2C72462234%2C72470440%2C72470899%2C72471280%2C72472051%2C72473841%2C72481458%2C72485656%2C72485658%2C72486593%2C72494250%2C72513422%2C72513513%2C72523972%2C72530239%2C72534000%2C72536387%2C72538597%2C72549171%2C72549174%2C72561417%2C72561423&hl=ko-KR&gl=kr&ssta=1&ts=CAESCgoCCAMKAggDEAAaHhIcEhQKBwjoDxAEGA8SBwjoDxAEGBAYATIECAAQACoHCgU6A0tSVw&qs=CAAgACgA&ap=KigKEglWdogmq6tBQBF8kGVhiiRgQBISCXPseYl8GUJAEXyQZSH_OmBAMABoAQ&ictx=111&ved=0CAAQ5JsGahcKEwjAxZq6k7-FAxUAAAAAHQAAAAAQdw"
    if request.method == 'POST':
        form = CheckinCheckoutForm(request.POST)
        if form.is_valid():
            checkin_date = form.cleaned_data['checkin_date']
            checkin_date_str = "{}월 {}".format(checkin_date.month, checkin_date.day)
            checkout_date = form.cleaned_data['checkout_date']
            checkout_date_str = "{}월 {}".format(checkout_date.month, checkout_date.day)
            AccomodationInfo.objects.all().delete()
            set_dates_and_crawl(gyeongJu_Accomodation_Url, 
                                checkin_date_str, checkout_date_str)
            data = AccomodationInfo.objects.all()  
        else:
            data = None
    else:
        form = CheckinCheckoutForm()
        data = None
    return render(request, 'GyeongJu/accomodation_index.html', {'form': form, 'data': data})
