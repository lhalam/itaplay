from django import forms
from authentication.models import AdviserUser


class AdviserUserForm(forms.Form):

    class Meta:
            model = AdviserUser
            fields = ('user', 'id_company', 'avatar')
