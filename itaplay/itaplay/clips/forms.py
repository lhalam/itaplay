from django import forms

class ClipForm(forms.Form):

    name_file = forms.CharField(max_length=128)
    clip_file = forms.FileField(label='Select a file')
    