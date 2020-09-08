from django import forms

from .models import Web

# class RawWebForm(forms.Form):
#     email = forms.CharField()
#     gender = forms.CharField()
#     subject = forms.CharField()
#     interested_things = forms.CharField()

class WebForm(forms.ModelForm):
    class Meta:
        model = Web
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'interested_things': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'email': 'Email',
            'gender': '性別',
            'subject': '收禮人',
            'interested_things': '喜歡的事物'
        }
