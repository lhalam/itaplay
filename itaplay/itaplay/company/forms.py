from django import forms
from models import Company

class CompanyForm(forms.Form):
        """
        Form for createing company.
        """
        class Meta:
            model = Company
            fields = ('id','company_zipcode', 'company_logo', 'company_name', "company_mail", 'company_phone',  'company_address', 'administrator')
