from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from company.models import Company


class AdviserUser(models.Model):
    """
    Model of user - contain foreign key to default Django user and have additional fields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    avatar = models.URLField(default="default-user-logo.png")

    @staticmethod
    def create_user(user_registration_form, invitation):
        """
        Function, that create new user
        :param user_registration_form: valid instance of UserRegistrationForm
        :param invitation: user invitation
        :return: nothing
        """
        base_user = user_registration_form.save(commit=False)
        base_user.username = invitation.email
        base_user.email = invitation.email
        base_user.set_password(user_registration_form.data['password'])
        base_user.save()

        user = AdviserUser()
        user.user = base_user
        user.id_company = invitation.id_company
        user.save()


class AdviserInvitations(models.Model):
    """Stores invitation data"""
    email = models.EmailField()
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField()
    used_time = models.DateTimeField(null=True, blank=True)

    def close_invitation(self):
        """
        Function for making invitation inactive and setting usage time
        :return: nothing
        """
        self.is_active = False
        self.used_time = timezone.now()
        self.save()

    @staticmethod
    def get_invitation(verification_code):
        """
        Function for finding invitation by verification code
        :param verification_code: verification code for user registration
        :return: invitation object of Invitation Model
        """
        invitation_query = AdviserInvitations.objects.filter(verification_code=verification_code)
        if invitation_query.exists():
            invitation = invitation_query.first()
            if not invitation.is_active:
                raise IndexError("Invitation is already used")
        else:
            raise IndexError("No open invitation")
        return invitation
