# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from utils.s3utils import ClipUploadAmazon


class Clip(models.Model, ClipUploadAmazon):

    """
    Model of clip.
    """

    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    clipfile = models.FileField(upload_to='', blank=True, null=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    mimetype = models.CharField(max_length=64, null=True, blank=True)

    def delete_clip(self, clip_id):
        """
        Method for deleting clip from database.
        :param pk: primary key for searched clip.
        :return: nothing.
        """

        Clip.objects.filter(id=clip_id).delete()

    def get_clip(self, clip_id):
        """
        Method for getting current clip from database.
        :param pk: primary key for searched clip.
        """
        return Clip.objects.filter(id=clip_id)

    def get_all_clips(self):
        """
        Method for getting all clips from database.
        :param pk: primary key for searched clip.
        """
        return Clip.objects.all()


# signal allows us delete media files from AWS S3 bucket
@receiver(models.signals.post_delete, sender=Clip)
def remove_file_from_s3(sender, instance, **kwargs):
    instance.clipfile.delete(save=False)
