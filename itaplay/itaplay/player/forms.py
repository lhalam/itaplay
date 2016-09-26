from django import forms
from models import Player

class PlayerForm(forms.Form):
        class Meta:
            model = Player
            fields = ('id','player_name', 'player_description', 'player_mac_address', "player_status",)
