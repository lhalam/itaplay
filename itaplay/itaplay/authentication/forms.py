from models import AdviserInvitations
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    """
    Form for registration user
    """
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=20, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password",
                                       min_length=6, max_length=20, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', "confirm_password")

    def clean_confirm_password(self):
        """
        Function checks that fields password and confirm_password are equal
        :return: nothing
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Your passwords do not match")
        return confirm_password

class InviteForm(forms.ModelForm):
    email = forms.EmailField(label="Invite email")
    company_id = forms.NumberInput()

    class Meta:
        model = AdviserInvitations
        fields = ('email', 'id_company')
