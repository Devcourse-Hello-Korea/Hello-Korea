from django.shortcuts import render
from .accomodation_models import AccomodationInfo, AccomodationForm_model
from .accomodation_forms import Accomodation_Form
from .accomodation_trans import translate_data

def accomodation_view(request):
    global data
    data = None
    form = Accomodation_Form()
    lang = request.COOKIES.get('user_lang', 'ko')
    form_data = AccomodationForm_model.objects.filter(lang=lang).first()
    if request.method == 'POST':
        selected_month = request.POST.get('month')
        selected_language = request.POST.get('Language')
        action = request.POST.get('action')
        print(selected_month, selected_language, action)

        if action == 'search':
            data = AccomodationInfo.objects.filter(lang=lang, month=selected_month)

        '''form = Accomodation_Form(request.POST)
        if form.is_valid():
            if 'action' in request.POST and request.POST['action'] == 'search':
                selected_month = form.cleaned_data['month']  # 선택된 월을 가져옴
                # 데이터베이스에서 해당 월에 해당하는 항목을 가져옴
                data = AccomodationInfo.objects.filter(lang=test_lang, month=selected_month)'''

    else:
        form = Accomodation_Form()
    return render(request, 'GyeongJu/accomodation_index.html', {'form' : form, 'data': data, 'form_data': form_data})
