from django import forms

class ClipForm(forms.Form):

    clip_file = forms.FileField(label='Select a file')
    