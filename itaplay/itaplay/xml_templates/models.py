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
        """Customizes representation of single template in admin."""
        return u"%s" % (self.template_name)

    def set(self, template_name, xml_file):
        """Sets values for instance of Template.

        Args:
            template_name: name of set template.
            xml_file: corresponds to template_content of Template.
        """
        self.template_name = template_name
        self.template_content = xml_file

    @classmethod
    def get_all(cls):
        """Returns all templates."""
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, template_id):
        """Retrieves single template by given id.

        Args:
            template_id: id of retrieved template.
        Returns:
            single template by given id.
        """
        return cls.objects.get(id=template_id)

    @classmethod
    def delete(cls, template_id):
        """Deletes single template by given id.

        Args:
            template_id: id of deleted template.
        """
        cls.objects.filter(pk=template_id).delete()
