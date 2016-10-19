# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
import boto
from boto.s3.connection import S3Connection
from django.conf import settings
from itaplay import local_settings
from itaplay.settings import MAX_CLIP_SIZE
from django.core.exceptions import ValidationError


def save_on_amazon_with_boto(clipfile):
    """Function that uploads clip on amazon

        Returns :
            str : url
    """
    if clipfile.size > MAX_CLIP_SIZE:
        raise ValidationError("Your file is too large. Please enter valid file")
    else:
        conn = S3Connection(local_settings.AWS_ACCESS_KEY_ID,
                            local_settings.AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        k = boto.s3.key.Key(bucket)
        k.key = settings.MEDIAFILES_LOCATION + clipfile.name
        # save on S3
        k.set_contents_from_file(clipfile)
        # make public
        k.set_acl('public-read')
        # generate url which will be save in database 
        url = k.generate_url(expires_in=0, query_auth=False)
        return url


def delete_from_amazon_with_boto(url):
    """Function that delete clip from amazon

        Returns : True
    """
    conn = S3Connection(local_settings.AWS_ACCESS_KEY_ID,
                        local_settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
    k = boto.s3.key.Key(bucket)
    filename_from_url = url.split('/')[-1]
    k.key = settings.MEDIAFILES_LOCATION + filename_from_url
    bucket.delete_key(k)
    return True
