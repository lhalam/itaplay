from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class AdviserUser(models.Model): # name of our project is Adviser
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    IdCompany = models.IntegerField() # will be foreign key
    avatar = models.URLField()

    def setUpUser(self, baseUser, invitation):
        self.user = baseUser
        self.avatar = "default-user-logo.png" # or should make default value on DB
        self.IdCompany = invitation.IdCompany


class AdviserInvitations(models.Model):
    email = models.EmailField()
    IdCompany = models.IntegerField()
    verificationCode = models.CharField(max_length=128)
    isActive = models.BooleanField()
    creationTime = models.DateTimeField()
    usedTime = models.DateTimeField()
