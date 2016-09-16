import boto
from storages.backends.s3boto import S3BotoStorage
from boto.s3.connection import S3Connection
from django.conf import settings
from itaplay import local_settings

StaticS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaS3BotoStorage = lambda: S3BotoStorage(location='media')

VALID_VIDEO_EXTENSIONS = [".mp4", ".avi", ".wmv", ".ogg", ]
VALID_IMAGE_EXTENSIONS = [".jpeg", ".jpg", ".png", ".svg", ".tiff", ".gif", ]

# Class for upload media files to Amazon 

class ClipUploadAmazon(object):

    """
    Handling save file on Amazon method.

    :return: True.
    """
    def save_on_amazon_with_boto(self):

        if self.clipfile:
            conn = S3Connection(local_settings.AWS_ACCESS_KEY_ID,
                                local_settings.AWS_SECRET_ACCESS_KEY)
            bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
            k = boto.s3.key.Key(bucket)
            k.key = settings.MEDIAFILES_LOCATION + self.clipfile.name
            k.set_contents_from_file(self.clipfile)

            url = k.generate_url(expires_in=0, query_auth=False)
            self.url = url
            print self.url
            if self.url.endswith(tuple(VALID_VIDEO_EXTENSIONS)):
                self.mimetype = "video/mp4"
            elif self.url.endswith(tuple(VALID_IMAGE_EXTENSIONS)):
                self.mimetype = "image/jpeg"
            else:
                raise ValidationError("Please enter valid file")
            return True
