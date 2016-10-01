import json

from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User


class LoginView(TestCase):

    def setUp(self):
        user = User.objects.create(username="test@test.com")
        user.set_password("rootroot")
        user.save()

        self.client = Client()

    def test_Authentication_get_login_page(self):
        response = self.client.get('/auth/login/?next=/')
        self.assertEqual(response.status_code, 200)

    def test_Authentication_post_login_success(self):
        user_data = json.dumps(
            {'username': "test@test.com", 'password': "rootroot"})

        response = self.client.post("/auth/login", data=user_data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_Authentication_post_login_failed_username(self):
        user_data = json.dumps({'username': "failed", 'password': "rootroot"})

        response = self.client.post("/auth/login", data=user_data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_Authentication_post_login_failed_password(self):
        user_data = json.dumps(
            {'username': "test@test.com", 'password': "failed"})

        response = self.client.post("/auth/login", data=user_data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 401)


class LogoutView(TestCase):

    def setUp(self):
        user = User.objects.create(username="test@test.com")
        user.set_password("rootroot")
        user.save()

        self.client = Client()

    def test_Authentication_get_login_page(self):
        self.client.login(username='test@test.com', password='rootroot')
        response = self.client.get('/auth/logout')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
