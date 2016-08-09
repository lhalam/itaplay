# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clip(models.Model):

      
    video = models.FileField(upload_to='clips/%Y/%m/%d')