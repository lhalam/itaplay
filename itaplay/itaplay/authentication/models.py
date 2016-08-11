from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class AdviserUser(models.Model):
    """
    Model of user - contain foreign key to default Django user and have additional fields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ID_company = models.IntegerField()  # will be foreign key
    avatar = models.URLField(default="default-user-logo.png")

    def __init__(self, user_registration_form, invitation):
        super(AdviserUser, self).__init__()

        base_user = user_registration_form.save(commit=False)
        base_user.username = invitation.email
        base_user.email = invitation.email
        base_user.set_password(user_registration_form.data['password'])
        base_user.save()

        self.user = base_user
        self.ID_company = invitation.id_company


class AdviserInvitations(models.Model):
    """Stores invitation data"""
    email = models.EmailField()
    id_company = models.IntegerField()
    verification_code = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField()
    used_time = models.DateTimeField(null=True, blank=True)
