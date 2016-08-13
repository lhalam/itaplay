# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clip(models.Model):
    
    name = models.CharField(max_length=128, null=True, blank=True)  
    video = models.FileField(upload_to='clips/%Y/%m/%d', blank=True, null=True)
    