from django import forms
from default.models import User_Info
class UserModelForm(forms.ModelForm):
    class Meta:
        model = User_Info
        fields = ['name','qqnum','telnum','mailnum','address',]