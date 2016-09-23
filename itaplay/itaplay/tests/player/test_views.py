from django.test import TestCase
from player.models import Player
from company.models import Company
from projects.models import AdviserProject
from django.test import Client
from django.forms.models import model_to_dict
import json
from django.core.urlresolvers import reverse


class PlayerViewTestCase(TestCase):

    def setUp(self):
        _company = Company(
            id=1,
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_phone="+380901234567",
        )
        _company.save()
        _project = AdviserProject(
            id=1,
            id_company=_company,
            name="project1",
            description="test",
            project_template="test",
            )
        _project.save()

        self.first = [Player.objects.create(
            id=1,
            name="player1",
            description="player description",
            mac_address="11:2a:bb:q1:ss:77",
            status=False,
            project=_project),
                Player.objects.create(
            id=2,
            name="player2",
            description="player2 description",
            mac_address="88:2a:bb:q1:ss:88",
            status=True,
            project=_project)
        ]

        self.client = Client()
        self.client.login(username="test@test.com", password="password")

    def test_get_list(self):
        url = reverse('players')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_player(self):
        url = reverse('player', args=[1])
        response = self.client.get(url)
        player = json.loads(response.content)["player"]
        self.assertEqual(player.get("id"), 1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('players')
        data = json.dumps({'name': 'TestPlayer', 'description': 'Player description',
                           'mac_address': "11:2a:bb:q1:ss:77", 'id': 4,'status': True})
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Player.objects.get(id=4).name, 'TestPlayer')
        self.assertEqual(Player.objects.get(id=4).description, 'Player description')
        self.assertEqual(Player.objects.get(id=4).mac_address, "11:2a:bb:q1:ss:77")

    def test_failed_post(self):
        url = reverse('players')
        data = json.dumps({'name': 'TestPlayer', 'description': 'Player description',
                           'mac_address': "11:2a:bb:q1:ss:77111111", 'id': 4, 'status': True})
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        url = reverse('player_delete', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Player.objects.all()), 1)

    def test_put(self):
        url = reverse('players')
        data = json.dumps({'id': 2, 'name': 'Put Player',
                           'description': "player2 description",
                           'mac_address': "88:2a:bb:q1:ss:88",
                           'status': True})
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Player.objects.get(id=2).name, 'Put Player')

    def test_failed_put(self):
        url = reverse('players')
        data = json.dumps({'name': 'TestPlayer', 'description': 'Player description',
                           'mac_address': "11:2a:bb:q1:ss:77111111", 'id': 1, 'status': True})
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)