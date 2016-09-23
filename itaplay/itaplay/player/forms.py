from django import forms
from models import Player


class PlayerForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=500)
    mac_address = forms.CharField(max_length=17)
    status = forms.BooleanField()

    class Meta:
        model = Player
        fields = ('id', 'name', 'description', 'mac_address', "status")
