import datetime
from django.test import TestCase
from company.models import Company
from authentication.models import AdviserInvitations

class AdviserInvitationsTest(TestCase):
    """
    Test cases for invitation model
    """

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

        AdviserInvitations.objects.create(
            email="mail2@mail.com",
            id_company=company,
            verification_code="12345678910",
            is_active=False,
            creation_time=datetime.datetime.now(),
            used_time=datetime.datetime.now()
        )

    def test_invite_get_by_email(self):
        """
        Ensure we can get invite by e-mail
        """
        invite = AdviserInvitations.objects.get(email="mail@mail.com")
        self.assertEqual(invite.email, "mail@mail.com")

    def test_close_invitation(self):
        """
        Ensure that close invitation functionality is working
        """
        invite = AdviserInvitations.objects.first()
        invite.close_invitation()
        modified_invite = AdviserInvitations.objects.first()
        self.assertEqual(modified_invite.is_active,False)

    def test_get_invitation(self):
        """
        Ensure that we can get invitation by unique code
        """
        invite = AdviserInvitations.get_invitation("123456789")
        self.assertEqual(invite.email, "mail@mail.com")

    def test_get_expired_invitation(self):
        """
        Ensure that getting expired invite raises index error with special message
        """
        with self.assertRaisesMessage(IndexError,"Invitation is already used"):
            invite = AdviserInvitations.get_invitation("12345678910")

    def test_get_fake_invitation(self):
        """
        Ensure that getting fake invite raises index error with special message
        """
        with self.assertRaisesMessage(IndexError,"No open invitation"):
            invite = AdviserInvitations.get_invitation("123456")


