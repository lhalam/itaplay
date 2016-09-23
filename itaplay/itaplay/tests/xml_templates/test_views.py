import json

from django.test import TestCase, Client
from xml_templates.models import XmlTemplate


class XmlTemplateViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_xml_templates_not_login(self):
        response = self.client.get('/#/templates')
        self.assertEqual(response.status_code, 302)

    # def test_get_xml_template_if_login(self):
    #     response = self.client.get('/#/templates')
    #     self.

    def test_login(self):
        user_data = json.dumps(
            {'username': 'test@test.com', 'password': 'password'})
        response = self

    # def test_xml_templates_list(self):
    #     self.login()
    #     self.url = "#/templates"
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, 200)

    # def login(self):
    #     user_data = json.dumps(
    #         {'username': "test@test.com", 'password': "rootroot"})

    #     self.client.post("/auth/login", data=user_data,
    #                      content_type='application/json', follow=True)
