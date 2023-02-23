from django import forms
from .models import Article



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'photo', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Названия'
            }),
            'content':forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }