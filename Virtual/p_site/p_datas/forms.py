from django import forms

class CheckinCheckoutForm(forms.Form):
    checkin_date = forms.DateField(label='체크인 날짜', widget=forms.TextInput(attrs={'type': 'date'}))
    checkout_date = forms.DateField(label='체크아웃 날짜', widget=forms.TextInput(attrs={'type': 'date'}))
