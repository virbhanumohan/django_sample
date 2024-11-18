from django.forms import ModelForm
from .models import Post
from django import forms

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','content']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=65)
    password=forms.CharField(max_length=65, widget=forms.PasswordInput)

