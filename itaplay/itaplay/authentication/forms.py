from models import AdviserInvitations
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    """
    Form for registration user
    """
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=20)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password",
                                       min_length=6, max_length=20)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', "confirm_password")

    def clean_confirm_password(self):
        """
        Function checks that fields password and confirm_password are equal
        :return: nothing
        """
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

class UserInvitationForm(forms.ModelForm):
    """
    Form for inviting users
    """
    email = forms.EmailField(label="Invite email")
    company_id = forms.NumberInput()

    class Meta:
        model = AdviserInvitations
        fields = ('email', 'id_company')
