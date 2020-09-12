from django import forms
from django.forms import Form

from .models import Web

# class RawWebForm(forms.Form):
#     email = forms.CharField()
#     gender = forms.CharField()
#     subject = forms.CharField()
#     interested_things = forms.CharField()

class WebForm(forms.Form):
    class Meta:
        model = Web
        fields = '__all__'


        # receivername=forms.TextInput(attrs={'class': 'form-control'})
        # email=forms.TextInput(attrs={'class': 'form-control'})
        # receiveage=forms.TextInput(attrs={'class': 'form-control'})
        # relationship=forms.TextInput(attrs={'class': 'form-control'})
            # 'budget': forms.Select(attrs={'class': 'form-control'})
        # labels = {
        #
        #     'email': 'Email',
        #     'gender': '性別',
        #     'subject': '收禮人',
        #     'interested_things': '喜歡的事物'
        # }
# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Web
# 		fields = '__all__'

