from authentication.models import AdviserInvitations
from company.models import Company
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    """
    Form for registration user
    """
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=20,
                               required=True)
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


class UserInvitationForm(forms.ModelForm):
    """
    Form for inviting users
    """
    email = forms.EmailField(widget=forms.EmailInput)
    id_company = forms.ModelChoiceField(queryset=Company.objects.all())

    class Meta:
        model = AdviserInvitations
        fields = ('email', 'id_company')


class LoginForm(forms.ModelForm):
    username = forms.EmailField()
    password = forms.CharField(min_length=6)

    class Meta:
        model = User
        fields = ('email', 'password')


