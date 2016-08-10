from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    """account for company"""
    company_logo = models.URLField( unique=True)
    company_name = models.CharField(max_length=200, unique=True)
    company_mail = models.EmailField(unique=True)
    company_phone = models.CharField(max_length=50, unique=True)
    company_address = models.CharField(max_length=200, unique=True)
    administrator = models.IntegerField(default=1) # will be foreign key
    