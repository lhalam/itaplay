from django import forms
from models import Clip


class ClipForm(forms.Form):

    class Meta:
            model = Clip
            fields = ('name', 'description', 'clipfile')
