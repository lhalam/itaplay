from __future__ import unicode_literals

from django.db import models

from company.models import Company


class AdviserProject(models.Model):
    """
    Model, that represent marketing projects
    """
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    project_template = models.TextField(blank=True, null=True)
