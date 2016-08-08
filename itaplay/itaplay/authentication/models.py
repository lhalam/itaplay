from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class AdviserUser(models.Model):    # name of our project is Adviser
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField()


class AdviserInvitations(models.Model):
    email = models.EmailField()
    id_company = models.IntegerField()
    verification_code = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField()
    used_time = models.DateTimeField(null=True, blank=True)
