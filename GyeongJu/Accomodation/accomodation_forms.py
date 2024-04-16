from django import forms
import datetime

class ChoiceMonthForm(forms.Form):
    # 현재 달을 기준으로 10개월간의 월 정보 생성
    def __init__(self, *args, **kwargs):
        super(ChoiceMonthForm, self).__init__(*args, **kwargs)
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year
        month_choices = []
        for i in range(11):  # 현재 달부터 +10개월간
            # 월과 연도 계산
            month = (current_month + i - 1) % 12 + 1
            year_offset = (current_month + i - 1) // 12
            year = current_year + year_offset
            month_choices.append((str(month), f'{year}년 {month}월'))
        
        self.fields['month'].choices = month_choices

    month = forms.ChoiceField(label='월 선택')
