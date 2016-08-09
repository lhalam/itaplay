from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


#change to underscore
class AdviserUser(models.Model): # name of our project is Adviser
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ID_company = models.IntegerField() # will be foreign key
    avatar = models.URLField()

    def setup_user(self, base_user, invitation):
        self.user = base_user
        self.avatar = "default-user-logo.png" # or should make default value on DB
        self.ID_company = invitation.IdCompany


class AdviserInvitations(models.Model):
    email = models.EmailField()
    IdCompany = models.IntegerField()
    verificationCode = models.CharField(max_length=128)
    isActive = models.BooleanField()
    creationTime = models.DateTimeField()
    usedTime = models.DateTimeField()
