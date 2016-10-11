from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(min_length=2, max_length=255, required=True)
    last_name = forms.CharField(min_length=2, max_length=255, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name')