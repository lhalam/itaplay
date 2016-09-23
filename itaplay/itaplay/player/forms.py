from django import forms
from models import Player


class PlayerForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=500)
    mac_address = forms.CharField(max_length=17, required=True)
    status = forms.BooleanField(required=True)

    class Meta:
        model = Player
        fields = ('id', 'name', 'description', 'mac_address', "status")
