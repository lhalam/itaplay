import json
from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse
from player.models import Player
from company.models import Company
from projects.models import AdviserProject


class MonitorViewTestCase(TestCase):

    def setUp(self):
        company = Company(
            id=1,
            zipcode="79008",
            logo="http://test.test",
            name="testcompany",
            mail="test@test.test",
            phone="+380901234567",
        )
        company.save()

        project = AdviserProject(
            id=1,
            id_company=company,
            name="project1",
            description="test",
            project_template="test",
        )
        project.save()

        Player.objects.create(
            id=1,
            name="player1",
            description="player description",
            mac_address="11:2a:bb:q1:ss:77",
            status=False,
            project=project  
        )

        Player.objects.create(
            id=2,
            name="player2",
            description="player description",
            mac_address="22:21:dd:ac:ff:22",
            status=False
        )

        self.client = Client()

    def test_get_rendered_monitor(self):
        url = reverse('monitor')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        
    def test_get_monitor(self):
        url = reverse('monitor_view', args=["11:2a:bb:q1:ss:77"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_head_monitor(self):
        url = reverse('monitor_view', args=["11:2a:bb:q1:ss:77"])
        response = self.client.head(url)
        self.assertEqual(response.status_code, 200)
    
    def test_head_monitor_without_project(self):
        url = reverse('monitor_view', args=["22:21:dd:ac:ff:22"])
        response = self.client.head(url)
        self.assertEqual(response.status_code, 204)