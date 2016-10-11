import json

from django.test import Client
from django.test import TestCase

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from player.models import Player
from projects.models import AdviserProject
from company.models import Company
from authentication.models import AdviserUser
from xml_templates.models import XmlTemplate


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

        User.objects.create(
            username="test3@test.com",
            is_superuser=True,
            email="test3@test.com",
            id=3
        )

        user = User.objects.get(id=1)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=2)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=3)
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

        AdviserUser.objects.create(
            user=User.objects.get(id=3),
            id_company=Company.objects.get(id=1),
            id=3
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

        XmlTemplate.objects.create(
            id=1,
            template_name='FirstTemplate',
            template_content="""<?xml version="1.0" encoding="UTF-8" ?>
                                            <project name="template1" height="100" width="100">
                                                <area id="1" left="10" top="10"  width="30" height="30">
                                                </area>
                                            </project>"""
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
        self.assertEqual(response.content, '{"count":1,"next":null,"previous":null,"results":[{"id":1,"id_company":1,'
                                           '"name":"TestProject","description":"Test description"}]}')

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

    def test_access_to_adviser_project(self):
        """
        Testing is AdviserProject inaccessible for user with others company ids
        """
        url = reverse('project', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_access_to_adviser_project_for_admin(self):
        """
        Ensure that admin has access to any AdviserProject
        :return:
        """
        url = reverse('project', args=[2])
        self.client.logout()
        self.client.login(username="test3@test.com", password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_to_adviser_project_list_for_admin(self):
        """
        Ensure that admin can get list of all AdviserProject
        """
        url = reverse('projects-list')
        self.client.logout()
        self.client.login(username="test3@test.com", password="password")
        response = self.client.get(url)
        self.assertEqual(response.content,
                         '{"count":2,"next":null,"previous":null,"results":[{"id":1,"id_company":1,'
                         '"name":"TestProject","description":"Test description"},{"id":2,"id_company":2,'
                         '"name":"TestProject 2","description":"Test description"}]}')

    def test_add_template_to_project(self):
        """
        Testing add template to project
        """
        user_data = json.dumps(
            {'template_id': 1,
             'project_id': "1",
             'areas': [{'id': 1,
                        'clips': [{'pk': 1,
                                   'fields': {
                                       'url': 'https://itaplayadviserireland.s3.amazonaws.com/media/Selection_004.png',
                                       'mimetype': 'image/jpeg',
                                       'name': 'MyClip1'}
                                   }]
                        }]
             })

        response = self.client.post("/api/projects/1/template/", data=user_data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)


class AdviserProjectsToPlayersTests(TestCase):

    def setUp(self):
        User.objects.create(
            username="test@superadmin.com",
            is_superuser=True,
            email="super@test.com",
            id=1
        )

        User.objects.create(
            username="test@test.com",
            is_superuser=False,
            email="test@test.com",
            id=2
        )

        User.objects.create(
            username="test3@test.com",
            is_superuser=False,
            email="test3@test.com",
            id=3
        )

        user = User.objects.get(id=1)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=2)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=3)
        user.set_password("password")
        user.save()

        Company.objects.create(
            id=1,
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_address= "testaddress",
            company_phone="+380901234567",
        )

        Company.objects.create(
            id=2,
            company_zipcode="794508",
            company_logo="http://test2.test",
            company_name="testcompany2",
            company_mail="test2@test.test",
            company_address="testaddress2",
            company_phone="+380901234677",
        )

        AdviserUser.objects.create(
            user=User.objects.get(id=2),
            id_company=Company.objects.get(id=1),
            id=1
        )

        AdviserUser.objects.create(
            user=User.objects.get(id=3),
            id_company=Company.objects.get(id=2),
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

        Player.objects.create(
            id=1,
            name="testPlayer 1",
            description="first player test description",
            mac_address="aa:dd:ff:11:22:33",
            status=True,
            project=AdviserProject.objects.get(id=1)
            )

        Player.objects.create(
            id=2,
            name="testPlayer 2",
            description="second player test description",
            mac_address="66:55:44:ad:fb:cc",
            status=False,
            project=AdviserProject.objects.get(id=1)
            )

        Player.objects.create(
            id=3,
            name="testPlayer 3",
            description="third player test description",
            mac_address="df:df:aa:aa:aa:cc",
            status=True,
            project=AdviserProject.objects.get(id=2)
            )

        Player.objects.create(
            id=4,
            name="testPlayer 4",
            description="third player test description",
            mac_address="fd:fd:cc:aa:32:cc",
            status=True,
            )

        self.client = Client()
        self.client.login(username="test@test.com", password="password")

    def test_get(self):
        url = reverse('get_players_for_project', args=[1])
        response = self.client.get(url)
        players = json.loads(response._container[0])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(players[0].get("id"), 2)
        self.assertEqual(players[1].get("id"), 1)

    def test_get_try_foreign_project(self):
        url = reverse('get_players_for_project', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        massage = response._container[0]
        self.assertEqual(massage, 'Permission denied')

    def test_put(self):
        url = reverse('put_projects_to_players')
        data = json.dumps({ 'project' : {
                                          'id' : 2,
                                          'name' : 'TestProject 2',
                                          'description' : 'Test description',
                                          'id_company' : 2
                                        },
                            'players' : [{
                                           'id' : 1,
                                           'name' : 'testPlayer 1',
                                           'description' : 'first player test description',
                                           'mac_address' : 'aa:dd:ff:11:22:33',
                                           'status': True,
                                        },
                                        {
                                           'id' : 4,
                                           'name' : 'testPlayer 4',
                                           'description' : 'player test description',
                                           'mac_address' : 'fd:fd:cc:aa:32:cc',
                                           'status': True,
                                        }],

        })
        self.client = Client()
        self.client.login(username="test3@test.com", password="password")
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        first_player = Player.objects.get(id=1)
        self.assertEqual(first_player.project.id, 2)
        second_player = Player.objects.get(id=4)
        self.assertEqual(second_player.project.id, 2)

    def test_put_try_foreign_project(self):
        data = json.dumps({ 'project' : {
                                          'id' : 2,
                                          'name' : 'TestProject 2',
                                          'description' : 'Test description',
                                          'id_company' : 2
                                        },
                            'players' : [{
                                           'id' : 1,
                                           'name' : 'testPlayer 1',
                                           'description' : 'first player test description',
                                           'mac_address' : 'aa:dd:ff:11:22:33',
                                           'status': True,
                                        },
                                        {
                                           'id' : 4,
                                           'name' : 'testPlayer 4',
                                           'description' : 'player test description',
                                           'mac_address' : 'fd:fd:cc:aa:32:cc',
                                           'status': True,
                                        }],

        })
        url = reverse('put_projects_to_players')
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        massage = response._container[0]
        self.assertEqual(massage, 'Permission denied')

    def test_put_try_without_players(self):
        invalid_data = json.dumps({ 'project' : {
                                          'id' : 1,
                                          'name' : 'TestProject 1',
                                          'description' : 'Test description',
                                          'id_company' : 1
                                        }})
        url = reverse('put_projects_to_players')
        response = self.client.put(url, data=invalid_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        massage = response._container[0]
        self.assertEqual(massage, 'Players are not added. Please, add some players.')

    def test_post_project_with_players(self):
        AdviserProject.objects.all().delete()
        url = reverse('projects-list')
        data = json.dumps({ 'id' : 2,
                            'name' : 'TestProject 2',
                            'description' : 'Test description',
                            'players' : [ 2, 3,],
        })
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AdviserProject.objects.count(), 1)
        first_player = Player.objects.get(id=2)
        self.assertEqual(first_player.project.id, 2)
        second_player = Player.objects.get(id=3)
        self.assertEqual(second_player.project.id, 2)
