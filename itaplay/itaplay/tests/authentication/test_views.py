import json, mock, datetime

from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
from authentication.models import AdviserUser, AdviserInvitations

from company.models import Company


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

class InviteView(TestCase):

    def setUp(self):
        company = Company.objects.create(
            id=1,
            zipcode="79008",
            logo="http://test.test",
            name="testcompany",
            mail="test@test.test",
            phone="+380901234567",
        )

        user = User.objects.create(username="test@test.com", email = "test@test.com")
        user.set_password("rootroot")
        user.save()

        adviser_user = AdviserUser.objects.create(user = user, id_company = company)
        adviser_user.save()

        adviser_invite = AdviserInvitations.objects.create(email = "test3@test.com", id_company = company,
                                                           verification_code = "1213", is_active = True,
                                                           creation_time = datetime.datetime.now())

        self.client = Client()

    @mock.patch('django.forms.forms.BaseForm.is_valid')
    def test_post_invite_page_succses(self, fakeresult):
        fakeresult.return_value = True
        self.client.login(username='test@test.com', password='rootroot')
        data = json.dumps(
            {'email': "test2@test.com", 'id_company': 1})

        response = self.client.post("/auth/invite", data=data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)

    @mock.patch('django.forms.forms.BaseForm.is_valid')
    def test_post_invite_page_invalid_form(self, fakeresult):
        fakeresult.return_value = False
        self.client.login(username='test@test.com', password='rootroot')
        data = json.dumps(
            {'email': "testtest.com", 'id_company': 1})

        response = self.client.post("/auth/invite", data=data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, "Invalid input data. Please edit and try again.")

    @mock.patch('django.forms.forms.BaseForm.is_valid')
    def test_post_invite_page_user_is_registered(self, fakeresult):
        fakeresult.return_value = True
        self.client.login(username='test@test.com', password='rootroot')
        data = json.dumps(
            {'email': "test@test.com", 'id_company': 1})

        response = self.client.post("/auth/invite", data=data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content,"User with this e-mail is registered")

    @mock.patch('django.forms.forms.BaseForm.is_valid')
    def test_post_invite_page_user_is_invited(self, fakeresult):
        fakeresult.return_value = True
        self.client.login(username='test@test.com', password='rootroot')
        data = json.dumps(
            {'email': "test3@test.com", 'id_company': 1})

        response = self.client.post("/auth/invite", data=data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, "User with this e-mail is already invited")


class RegisterView(TestCase):
    """
    Tests for Registration View
    """

    def setUp(self):
        company = Company.objects.create(
            id=1,
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_phone="+380901234567",
        )

        user = User.objects.create(username="test@test.com", email="test@test.com")
        user.set_password("rootroot")
        user.save()

        adviser_user = AdviserUser.objects.create(user=user, id_company=company)
        adviser_user.save()

        adviser_invite = AdviserInvitations.objects.create(email="test3@test.com", id_company=company,
                                                           verification_code="1", is_active=True,
                                                           creation_time=datetime.datetime.now(),
                                                           id=1)

        self.client = Client()

    def test_opening_registration_form(self):
        """
        Ensure we can open registration form with valid verification_code
        """
        verification_code = AdviserInvitations.objects.get(id=1).verification_code
        response = self.client.get("/auth/register?code=" + verification_code)
        self.assertEqual(response.status_code, 200)

    def test_access_for_registration_form_with_wrong_verification_code(self):
        """
        Ensure we can not open registration form with wrong verification_code
        """
        verification_code = "0"
        response = self.client.get("/auth/register?code=" + verification_code)
        self.assertEqual(response.status_code, 400)

    def test_access_for_registration_form_without_verification_code(self):
        """
        Ensure we can not open registration form without verification_code
        """
        response = self.client.get("/auth/register")
        self.assertEqual(response.status_code, 400)

    def test_access_for_registration_form_with_closed_verification_code(self):
        """
        Ensure we can not open registration form with closed verification_code
        """
        verification_code = AdviserInvitations.objects.get(id=1).verification_code
        AdviserInvitations.objects.get(id=1).close_invitation()
        response = self.client.get("/auth/register?code=" + verification_code)
        self.assertEqual(response.status_code, 400)

    def test_creating_user(self):
        """
        Ensure we can create AdviserUser
        """
        verification_code = AdviserInvitations.objects.get(id=1).verification_code
        test_user = json.dumps({"first_name": "Test", "last_name": "Test", "password": "password",
                                "confirm_password": "password"})

        response = self.client.post("/auth/register?code=" + verification_code, data=test_user,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_creating_user_with_different_passwords(self):
        """
        Ensure we can not create AdviserUser with different passwords
        """
        verification_code = AdviserInvitations.objects.get(id=1).verification_code
        test_user = json.dumps({"first_name": "Test", "last_name": "Test", "password": "password",
                                "confirm_password": "password123"})

        response = self.client.post("/auth/register?code=" + verification_code, data=test_user,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
