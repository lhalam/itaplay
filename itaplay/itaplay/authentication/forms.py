from models import AdviserUser
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AdviserUserForm(forms.ModelForm):
    class Meta:
        model = AdviserUser
        fields = ('avatar',)