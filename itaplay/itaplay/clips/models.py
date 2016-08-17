# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Clip(models.Model):
    """
    Model of clip.
    """
    
    name = models.CharField(max_length=128, null=True, blank=True)  
    video = models.FileField(upload_to='clips/%Y/%m/%d', blank=True, null=True)
    

    def delete_clip(self, pk):
        """
        Method for deleteing clip from database.
        :param pk: primary key for searched company.
        :return: nothing.
        """
        Clip.objects.filter(pk = pk).delete()
    

    def get_clip(self, pk):
        """
        Method for getting current clip from database.
        :param pk: primary key for searched clip.
        
        """
        return Clip.objects.filter(pk = pk)

    def save_clip(self, *args, **kwargs):
        """
        Method for saving current clip to database.

        """
        super(Clip, self).save(*args, **kwargs)

    def get_all_clips(self):
        """
        Method for getting all clips from database.
        :param pk: primary key for searched clip.
        
        """
        return Clip.objects.all()
        

        