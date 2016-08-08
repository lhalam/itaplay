from django import forms

class ClipForm(forms.Form):

    #title_file = forms.CharField()
    #description_file = forms.CharField()
    clip_file = forms.FileField(label='Select a file')