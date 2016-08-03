from models import AdviserUser
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.EmailField(label="User name (e-mail):")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

class AdviserUserForm(forms.ModelForm):
    avatar = forms.URLField(label="Avatar (URL):")
    class Meta:
        model = AdviserUser
        fields = ('avatar',)