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
    project_hash = models.TextField(blank=True, null=True)

    @staticmethod
    def create(*args, **kwargs):
        """
        Create new AdviserUser
        :return: AdviserUser instance
        """
        adviser_project = AdviserProject.objects.create(*args, **kwargs)
        adviser_project.save()
        return adviser_project

    @staticmethod
    def get(id):
        """
        Get AdviserProject by id
        :param id: id of AdviserProject
        :return: AdviserProject instance
        """
        adviser_project = AdviserProject.objects.get(id=id)
        return adviser_project

    @staticmethod
    def filter(*args, **kwargs):
        """
        Get several AdviserProject
        :return: list of AdviserProjects
        """
        adviser_projects = AdviserProject.objects.filter(*args, **kwargs)
        return adviser_projects

    def delete(self, *args, **kwargs):
        """
        Delete AdviserProject
        :return deleted AdviserProjects and its count
        """
        return super(AdviserProject, self).delete(*args, **kwargs)

    @staticmethod
    def update(id, **kwargs):
        """
        Update fields of AdviserProject
        :param id: id of AdviserProject
        :return: updated AdviserProject
        """
        adviser_project = AdviserProject.get(id)
        adviser_project.name = kwargs.get("name", adviser_project.name)
        adviser_project.description = kwargs.get("description", adviser_project.description)
        adviser_project.project_template = kwargs.get("project_template", adviser_project.project_template)
        adviser_project.project_hash = kwargs.get("project_hash", adviser_project.project_hash)
        adviser_project.save()
        return adviser_project

