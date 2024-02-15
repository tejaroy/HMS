from django import forms
from .models import *

# class UsersModelForm(forms.ModelForm):
#     class Meta:
#         model = Users
#         fileds = '__all__'
#         exclude = ('created_at','updated_at')

class UsersForm(forms.Form):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    phone = forms.CharField(required =True)
    password = forms.CharField(required=True)
    is_active = forms.BooleanField(required=True)
    valid_date = forms.DateField(required=True)
