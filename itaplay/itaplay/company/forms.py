"""
Forms for company.
"""
from django import forms
from company.models import Company

class CompanyForm(forms.Form):
    """
    Form for createing company.
    """
    zipcode = forms.CharField(max_length=20, required=True)
    logo = forms.URLField(required=True)
    name = forms.CharField(max_length=200, required=True)
    mail = forms.EmailField(required=True)
    phone = forms.CharField(max_length=50, required=True)
    address = forms.CharField(max_length=200, required=True)
    
    class Meta:
        model = Company
        fields = ('id','zipcode', 'logo', 'name', "mail", 'phone',  'address', 'administrator')
