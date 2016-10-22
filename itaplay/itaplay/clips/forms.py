from django import forms
from models import Clip


class ClipForm(forms.Form):
    """
        Form for creating clip.
    """

    class Meta:
            model = Clip
            fields = ('name', 'description', 'clipfile')
