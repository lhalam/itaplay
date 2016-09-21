from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from projects.models import AdviserProject
from company.models import Company
from authentication.models import AdviserUser


class AdviserProjectsTests(APITestCase):
    def setUp(self):
        Company.objects.create(
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_phone="+380901234567",
            id=1
        )

        Company.objects.create(
            company_zipcode="794508",
            company_logo="http://test2.test",
            company_name="testcompany2",
            company_mail="test2@test.test",
            company_phone="+380901234677",
            id=2
        )

        User.objects.create(
            username="test@test.com",
            email="test@test.com",
            id=1
        )

        User.objects.create(
            username="test2@test.com",
            email="test2@test.com",
            id=2
        )

        user = User.objects.get(id=1)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=2)
        user.set_password("password")
        user.save()

        AdviserUser.objects.create(
            user=User.objects.get(id=1),
            id_company=Company.objects.get(id=1),
            id=1
        )

        AdviserUser.objects.create(
            user=User.objects.get(id=2),
            id_company=Company.objects.get(id=1),
            id=2
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
            id_company=Company.objects.get(id=2),
            id=2
        )

        self.client = APIClient()
        self.client.login(username="test@test.com", password="password")

    def test_create_adviser_project(self):
        """
        Ensure we can create a new AdviserProject object.
        """
        AdviserProject.objects.all().delete()
        url = reverse('projects-list')
        data = {'name': 'TestProject', 'description': 'Test description', 'id_company': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AdviserProject.objects.count(), 1)
        self.assertEqual(AdviserProject.objects.get().name, 'TestProject')
        self.assertEqual(AdviserProject.objects.get().description, 'Test description')
        self.assertEqual(AdviserProject.objects.get().id_company, Company.objects.get(id=1))

    def test_getting_list_of_adviser_project(self):
        """
        Ensure we can get list of AdviserProjects
        """
        url = reverse('projects-list')
        response = self.client.get(url)
        self.assertEqual(response.data, {'count': 1, "next": 'null', "previous": 'null', "results":
            [{"id": 1, "id_company": 1, "name": "TestProject", "description": "Test description"}]})

    def test_getting_adviser_project(self):
        """
        Ensure we can get info about AdviserProject
        """
        url = reverse('project', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.data, {'id': 1, 'name': 'TestProject', 'description': 'Test description',
                                         'id_company': 1})

    def test_updating_adviser_project(self):
        """
        Ensure we can update info about AdviserProject
        """
        url = reverse('project', args=[1])
        data = {'name': 'TestProjectChanged', 'description': 'Test description changed', 'id_company': 1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AdviserProject.objects.get(id=1).name, 'TestProjectChanged')
        self.assertEqual(AdviserProject.objects.get(id=1).description, 'Test description changed')
        self.assertEqual(AdviserProject.objects.get(id=1).id_company, Company.objects.get(id=1))

    def test_deleting_adviser_project(self):
        """
        Ensure we can delete AdviserProject
        """
        url = reverse('project', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AdviserProject.objects.count(), 1)

    def test_changing_company_of_adviser_project(self):
        """
        Ensure we can't change Company of AdviserProject
        """

        url = reverse('project', args=[1])
        data = {'name': 'TestProjectChanged', 'description': 'Test description changed', 'id_company': 2}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AdviserProject.objects.get(id=1).id_company, Company.objects.get(id=1))

    def test_access_adviser_project_list(self):
        """
        Testing is AdviserProjects are filtered by user company
        """
        url = reverse('projects-list')
        response = self.client.get(url)
        self.assertEqual(response.data,
                         {'count': 1, "next": 'null', "previous": 'null', "results":
                             [{"id": 1, "id_company": 1, "name": "TestProject", "description": "Test description"}]})
        self.client.logout()
        self.client.login(user="test2@test.com", password="password")
        response = self.client.get(url)
        self.assertEqual(response.data, {'count': 1, "next": 'null', "previous": 'null', "results":
            [{"id": 2, "id_company": 2, "name": "TestProject 2", "description": "Test description"}]})

    def test_access_to_adviser_project(self):
        """
        Testing is AdviserProject inaccessible for user with others company ids
        """
        url = reverse('project', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
