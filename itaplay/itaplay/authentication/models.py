from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class AdviserUser(models.Model): # name of our project is Adviser
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField()

