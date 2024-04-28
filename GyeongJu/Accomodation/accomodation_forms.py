import datetime
from django import forms

class Accomodation_Form(forms.Form):
    month = forms.ChoiceField(label='Select date')
    country = forms.ChoiceField(label='Language', choices=[
        ['ko', '한국어'],
        ['en', 'English'],
        ['ja', '日本語'],
        ['zh-tw', '繁體字'],
        ['zh-cn', '簡體字'],
        ['de', 'Deutsch'],
        ['ru', 'русский']
    ])
    
    # 현재 달을 기준으로 10개월간의 월 정보 생성
    def __init__(self, *args, **kwargs):
        super(Accomodation_Form, self).__init__(*args, **kwargs)
        # 함수 호출로 월 선택 필드의 선택지 설정
        self.fields['month'].choices = create_month_choices()

# 월 선택 필드의 선택지를 생성하는 함수
def create_month_choices():
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    month_choices = []
    for i in range(11):  # 현재 달부터 +10개월간
        # 월과 연도 계산
        month = (current_month + i - 1) % 12 + 1
        year_offset = (current_month + i - 1) // 12
        year = current_year + year_offset
        month_choices.append((str(month), f'{year} - {month}'))
    return month_choices
