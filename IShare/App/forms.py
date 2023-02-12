from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        # fields='__all__'
        fields=['username','email','password1','first_name']
    

    