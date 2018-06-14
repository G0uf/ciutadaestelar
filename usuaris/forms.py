from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    usuari=forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder':'Introdueix el teu usuari','autofocus':'autofocus'}))
    contrasenya=forms.CharField(min_length=6, max_length=50, widget=forms.PasswordInput)
    
class RegistreForm(forms.Form):
    usuari=forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder':'Introdueix el teu usuari','autofocus':'autofocus'}))
    correu=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Introdueix el teu usuari','autofocus':'autofocus'}))
    contrasenya=forms.CharField(min_length=6, max_length=50, widget=forms.PasswordInput)
    contrasenya_repetir=forms.CharField(min_length=6, max_length=50, widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['usuari']
        if User.objects.filter(username=username):
            raise forms.ValidationError('nom de usuari ja esta ocupat')
        return username

    def clean_email(self):
        correu = self.cleaned_data['correu']
        if User.objects.filter(email=correu):
            raise forms.ValidationError('El correu electronic ja esta registrat')
        return correu
        
class CanviarContrasenyaForm(forms.Form):
    contrasenya = forms.CharField(min_length=5, max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Introdueix la nova contrasenya'}))
    contrasenya_repetir = forms.CharField(min_length=5, max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Repeteix el teu nova contrasenya'}))