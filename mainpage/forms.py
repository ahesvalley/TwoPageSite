from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Profile




class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthday', 'about')
        labels = {
                "birthday": ("Дата Рождения    "),
                "about": ("О себе   "),
                }