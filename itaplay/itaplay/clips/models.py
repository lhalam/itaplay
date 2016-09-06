# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import boto
from django.conf import settings
from itaplay import local_settings


VALID_VIDEO_EXTENSIONS = [".mp4",".avi", ".wmv", ".ogg",]
VALID_IMAGE_EXTENSIONS = [".jpeg",".jpg",".png",".svg",".tiff", ".gif",]


class Clip(models.Model):
    """
    Model of clip.
    """

    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)  
    video = models.FileField(upload_to='', blank=True, null=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    mimetype = models.CharField(max_length=64, null=True, blank=True)
    

    def delete_clip(self, clip_id):
        """
        Method for deleteing clip from database.
        :param pk: primary key for searched clip.
        :return: nothing.
        """

        Clip.objects.filter(id = clip_id).delete()
    

    def get_clip(self, clip_id):
        """
        Method for getting current clip from database.
        :param pk: primary key for searched clip.
        
        """
        return Clip.objects.filter(id = clip_id)

    def save_clip(self, *args, **kwargs):
        
        if self.video:
            conn = boto.s3.connection.S3Connection(
                                local_settings.AWS_ACCESS_KEY_ID,
                                local_settings.AWS_SECRET_ACCESS_KEY)
            bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
            k = boto.s3.key.Key(bucket)
            k.key = settings.MEDIAFILES_LOCATION + self.video.name

            url = k.generate_url(expires_in=0, query_auth=False)
            self.url = url
            print self.url
            if self.url.endswith(tuple(VALID_VIDEO_EXTENSIONS)):
                self.mimetype = "video/mp4"
            elif self.url.endswith(tuple(VALID_IMAGE_EXTENSIONS)):
                self.mimetype = "image/jpeg"
            else:
                raise ValidationError("Please enter valid date")
        super(Clip, self).save(*args, **kwargs)
        



    def get_all_clips(self):
        """
        Method for getting all clips from database.
        :param pk: primary key for searched clip.
        
        """
        return Clip.objects.all()


# signal allows ud delete media files from AWS S3 bucket
@receiver(models.signals.post_delete, sender=Clip)
def remove_file_from_s3(sender, instance, **kwargs):
    instance.video.delete(save=False)

