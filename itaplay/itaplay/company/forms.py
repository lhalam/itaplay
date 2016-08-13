from django import forms

class CompanyForm(forms.Form):
    company_zipcode = forms.CharField(max_length=20, default="")
    company_logo = forms.URLField(default="")
    company_name = forms.CharField(max_length=200, unique=True)
    company_mail = forms.EmailField(unique=True)
    company_phone = forms.CharField(max_length=50, unique=True)
    company_address = forms.CharField(max_length=200)
    administrator = forms.IntegerField(default=1)