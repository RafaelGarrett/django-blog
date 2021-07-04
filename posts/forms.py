from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'conteudo', 'data')
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'data': forms.DateInput(attrs={
                'class': 'datepicker',
                'placeholder': '2021-03-07'
            })
        }