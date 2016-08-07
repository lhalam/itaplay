from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class AdviserUser(models.Model): # name of our project is Adviser
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField()


class AdviserInvitations(models.Model):
    email = models.EmailField()
    IdCompany = models.IntegerField()
    verificationCode = models.CharField(max_length=128)
    isActive = models.BooleanField(default=True)
    creationTime = models.DateTimeField()
    usedTime=models.DateTimeField(null=True, blank=True)
