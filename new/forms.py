from django import forms
from .models import NewArticle, Category

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewArticle
        fields = ['title', 'content', 'image', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержимое'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }