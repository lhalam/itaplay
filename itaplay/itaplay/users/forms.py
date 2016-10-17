from django import forms
from authentication.models import AdviserUser
from django.contrib.auth.models import User

class AdviserUserForm(forms.Form):

    class Meta:
            model = AdviserUser
            fields = ('user', 'id_company', 'avatar')


class UserForm(forms.ModelForm):
    first_name = forms.CharField(min_length=2, max_length=255, required=True)
    last_name = forms.CharField(min_length=2, max_length=255, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

