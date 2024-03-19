from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from .models import *

# class registerForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['name','email','mobile','passwd','address','profile']
    
#     def save(self):
#         s=super().save(commit=False)
#         s.password=make_password(self.cleaned_data['password'])
#         s.save()
#         return s

# class createuserform(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['username','password'] 

# class createorderform(ModelForm):
#     class Meta:
#         model=Order
#         fields="__all__"
#         exclude=['status']
# class registerForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','first_name','last_name','password','email']
    
#     def save(self):
#         s=super().save(commit=False)
#         s.password=make_password(self.cleaned_data['password'])
#         s.save()
#         return s

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
    

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields='__all__'
        
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s


class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

