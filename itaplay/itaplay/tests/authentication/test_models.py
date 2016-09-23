import datetime
from django.test import TestCase
from company.models import Company
from authentication.models import AdviserInvitations

class AdviserInvitationsTest(TestCase):

    def setUp(self):
        company = Company.objects.create(
            id = 1,
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_phone="+380901234567",
        )
        AdviserInvitations.objects.create(
            email="mail@mail.com",
            id_company= company,
            verification_code = "123456789",
            is_active = True,
            creation_time = datetime.datetime.now(),
            used_time = datetime.datetime.now()
        )

    def test_invite_get_by_email(self):
        invite = AdviserInvitations.objects.get(email="mail@mail.com")
        self.assertEqual(invite.email, "mail@mail.com")
