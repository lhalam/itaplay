from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class AdviserUser(models.Model):
    """
    Model of user - contain foreign key to default Django user and have additional fields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ID_company = models.IntegerField() # will be foreign key
    avatar = models.URLField(default="default-user-logo.png")

    def setup_user(self, base_user, invitation):
        """
        Function for filling additional data for this class
        :param base_user: default Django user
        :param invitation: invitation for user
        :return: nothing
        """
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
