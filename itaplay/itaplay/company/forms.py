from django import forms
from models import Company

class CompanyForm(forms.Form):
        """
        Form for createing company.
        """
        company_zipcode = forms.CharField(max_length=20, required=True)
        company_logo = forms.URLField(required=True)
        company_name = forms.CharField(max_length=200, required=True)
        company_mail = forms.EmailField(required=True)
        company_phone = forms.CharField(max_length=50, required=True)
        company_address = forms.CharField(max_length=200, required=True)
        
        class Meta:
            model = Company
            fields = ('id','company_zipcode', 'company_logo', 'company_name', "company_mail", 'company_phone',  'company_address', 'administrator')
