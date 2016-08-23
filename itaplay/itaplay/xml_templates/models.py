from __future__ import unicode_literals
from django.db import models


class XmlTemplate(models.Model):
    """Xml Template Model"""

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

    # @classmethod
    def set_xml_template(self, template_name, xml_file):
        self.template_name = template_name
        self.template_content = xml_file

    @classmethod
    def get_xml_templates_list(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, pk):
        return cls.objects.filter(pk=pk)

    @classmethod
    def delete_xml_template(cls, pk):
        return cls.objects.filter(pk=pk).delete()
