from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Digite seu nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),   
        }