from django.forms import ModelForm
from django import forms
from users_manager.models import User

class SignupForm(ModelForm):
    class Meta:
        user_name=forms.CharField()
        last_name=forms.CharField()
        nick_name=forms.CharField()
        user_email=forms.EmailField()
        password=forms.CharField(widget=forms.PasswordInput)
        user_age=forms.IntegerField()
        model=User
        widgets={
            'user_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'nick_name': forms.TextInput(attrs={'placeholder': 'Nickname'}),
            'user_email': forms.TextInput(attrs={'placeholder': 'Correo electronico'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Contraseña'}),
            'user_age': forms.TextInput(attrs={'placeholder': 'Edad'}),
        }
        fields='__all__'
