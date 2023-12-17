from django import forms
from .models import Album
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _


class Albumform(forms.ModelForm):

    class Meta:
        model=Album
        fields=['id','photo','classification']
        labels={'photo':''}



class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(label='username',required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
        
    }))

    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={
        'class':'form-control',
         
    }))

    password1=forms.CharField(label='password1',required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
       
        

    }))
    password2=forms.CharField(label='confirm password(again)',required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
      
    }))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}

class UserLoginForm(AuthenticationForm):

    username=UsernameField(widget=forms.TextInput(attrs={
        'autofocus':True,
        'class':'form-control',
       
    
    }))

    password=forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={
        'autocomplete':'current-password',
        'class':'form-control',
    }))