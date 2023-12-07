from django import forms
from .models import Album
from django.contrib.auth.models import User

class Albumform(forms.ModelForm):
    class Meta:
        model=Album
        fields=['id','photo','classification']