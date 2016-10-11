from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models

# Create your models here.


class MyUser(User):
    def set_user(self, data):
        self.first_name = data.get('first name', self.first_name)
        self.last_name = data.get('last name', self.last_name)
        self.save()

    class Meta:
        proxy = True