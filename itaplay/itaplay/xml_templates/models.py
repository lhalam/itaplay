from __future__ import unicode_literals

from django.db import models


# Create your models here.
class XmlTemplate(models.Model):
    """XmlTemplate Model"""

    class Meta(object):
        verbose_name = "Xml Template"
        verbose_name_plural = "Xml Templates"

    template_name = models.CharField(
        max_length=128,
        blank=False,
        verbose_name="name")

    template_content = models.TextField(
        blank=False,
        verbose_name="content")

    def __unicode__(self):
        return u"%s" % (self.template_name)
