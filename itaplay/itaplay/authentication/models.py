from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class AdviserUser(models.Model): # name of our project is Adviser
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ID_company = models.IntegerField() # will be foreign key
    avatar = models.URLField()

    def setUpUser(self, baseUser, invitation):
        self.user = baseUser
        self.avatar = "default-user-logo.png" # or should make default value on DB
        self.ID_company = invitation.ID_company

class AdviserInvitations(models.Model):
    email=models.EmailField()
    ID_company=models.IntegerField()
    verification_code=models.CharField(max_length=128)
    is_active=models.BooleanField()