import json

from django.test import TestCase, Client
from xml_templates.models import XmlTemplate
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse


class XmlTemplateViewTests(TestCase):

    def setUp(self):

        User.objects.create(
            id=1,
            username="superuser@user.com",
            email="super@user.com",
            password="password1",
            is_superuser=True,
        )

        User.objects.create(
            id=2,
            username="user@user.com",
            email="user@user.com",
            password="password2",
            is_superuser=False)

        self.client = Client()

        def test_get_list_xml_templates_loads(self):
            self.client.login(username="superuser@user.com",
                              password="password1")
            url = reverse('templates_list')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)


