from django.test import TestCase

from projects.models import AdviserProject
from company.models import Company


class AdviserProjectsModelTests(TestCase):
    def setUp(self):
        Company.objects.create(
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_phone="+380901234567",
            id=1
        )

        AdviserProject.objects.create(
            name="TestProject",
            description="Test description",
            id_company=Company.objects.get(id=1),
            id=1
        )

        AdviserProject.objects.create(
            name="TestProject 2",
            description="Test description",
            id_company=Company.objects.get(id=1),
            id=2
        )

        AdviserProject.objects.create(
            name="TestProject 3",
            description="Another test description",
            id_company=Company.objects.get(id=1),
            id=3
        )

    def test_creating_project(self):
        """
        Ensure we can create AdviserProjects
        """
        adviser_project = AdviserProject.create(id=8, id_company=Company.objects.get(id=1),
                                                name="Test creating project", description="Test description")
        self.assertEqual(adviser_project, AdviserProject.objects.get(id=8))

    def test_getting_project_by_id(self):
        """
        Ensure we can get AdviserProjects by id
        """
        adviser_project = AdviserProject.get(1)
        self.assertEqual(adviser_project, AdviserProject.objects.get(id=1))

    def test_deleting_project(self):
        """
        Ensure we can delete AdviserProject by id
        """
        adviser_project = AdviserProject.objects.get(id=1)
        adviser_project.delete()
        self.assertEqual(AdviserProject.objects.count(), 2)

    def test_filtering_projects(self):
        """
        Ensure we can filter AdviserProjects
        """
        adviser_projects = AdviserProject.filter(description="Test description")
        self.assertEqual(adviser_projects.count(),
                         AdviserProject.objects.filter(description="Test description").count())

    def test_updating_project_info(self):
        """
        Ensure we can update fields of AdviserProject
        """
        updated_project = AdviserProject.update(1, name="Updated project", description="Updated description")
        self.assertEqual(updated_project.name, AdviserProject.objects.get(id=1).name)
        self.assertEqual(updated_project.description, AdviserProject.objects.get(id=1).description)
