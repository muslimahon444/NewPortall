from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес электронной почты'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
        }

    