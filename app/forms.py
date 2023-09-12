from typing import Any
from django import forms
from django.core import validators
class Jspider(forms.Form):
    Iname= forms.CharField(max_length=50)
    Sname= forms.CharField(max_length=50)
    Sid= forms.IntegerField()
    Smail= forms.EmailField()
    Rmail= forms.EmailField()
    Join= forms.DateField()
    Sphone= forms.CharField(max_length=10, min_length=10, validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher= forms.CharField(max_length=50, widget= forms.HiddenInput, required=False)

    def clean(self):
        E= self.cleaned_data['Smail']
        RE= self.cleaned_data['Rmail']

        if(E != RE):
            raise forms.ValidationError('Invalid Email')
    
    def clean_botcatcher(self):
        bot= self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('Bot Catch')