from models import AdviserUser
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=20)
    confirmPassword = forms.CharField(widget=forms.PasswordInput, label="Confirm password", min_length=6, max_length=20)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'confirmPassword')

    def clean_confirmPassword(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirmPassword')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2