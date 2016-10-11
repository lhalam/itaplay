import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from company.models import Company
from authentication.models import AdviserInvitations
from authentication.models import AdviserUser
from authentication.forms import UserRegistrationForm

class AdviserInvitationsTest(TestCase):
    """
    Test cases for invitation model
    """

    def setUp(self):
        company = Company.objects.create(
            id = 1,
            zipcode="79008",
            logo="http://test.test",
            name="testcompany",
            mail="test@test.test",
            phone="+380901234567",
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


class AdviserUserTest(TestCase):
    """
    Tests for AdviserUser model
    """

    def setUp(self):
        Company.objects.create(
            zipcode="79008",
            logo="http://test.test",
            name="testcompany",
            mail="test@test.test",
            phone="+380901234567",
            id=1
        )

        AdviserInvitations.objects.create(
            email="mail@mail.com",
            id_company=Company.objects.get(id=1),
            verification_code="1",
            is_active=True,
            creation_time=datetime.datetime.now(),
            id=1
        )

        User.objects.create(
            username="test@test.com",
            email="test@test.com",
            id=10
        )

        User.objects.create(
            username="test2@test.com",
            email="test2@test.com",
            id=20
        )

        User.objects.create(
            username="test3@test.com",
            email="test3@test.com",
            id=30
        )

        user = User.objects.get(id=10)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=20)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=30)
        user.set_password("password")
        user.save()

        AdviserUser.objects.create(
            user=User.objects.get(id=10),
            id_company=Company.objects.get(id=1),
            id=10
        )

        AdviserUser.objects.create(
            user=User.objects.get(id=20),
            id_company=Company.objects.get(id=1),
            id=20
        )

    def test_creating_adviser_user(self):
        """
        Ensure we can create AdviserUser
        """
        adviser_user = AdviserUser.create(id=8, id_company=Company.objects.get(id=1),
                                          user=User.objects.get(id=30), avatar="Test")
        self.assertEqual(adviser_user, AdviserUser.objects.get(id=8))

    def test_creating_adviser_user_on_invitation_and_form(self):
        """
        Ensure we can crate AdviserUser using AdviserInvitation and Form
        """
        test_user = {"first_name": "Test", "last_name": "Test", "password": "password",
                     "confirm_password": "password"}
        registration_form = UserRegistrationForm(test_user)
        adviser_user = AdviserUser.create_user(registration_form, AdviserInvitations.objects.get(id=1))
        self.assertEqual(adviser_user, AdviserUser.objects.get(id=adviser_user.id))

    def test_getting_adviser_user_by_id(self):
        """
        Ensure we can get AdviserUsers by id
        """
        adviser_user = AdviserUser.get(10)
        self.assertEqual(adviser_user, AdviserUser.objects.get(id=10))

    def test_deleting_adviser_user(self):
        """
        Ensure we can delete AdviserUser by id
        """
        adviser_user = AdviserUser.objects.get(id=10)
        adviser_user.delete()
        self.assertEqual(AdviserUser.objects.count(), 1)

    def test_filtering_adviser_users(self):
        """
        Ensure we can filter AdviserUsers
        """
        adviser_users = AdviserUser.filter()
        self.assertEqual(adviser_users.count(),
                         AdviserUser.objects.filter().count())

    def test_updating_adviser_user_info(self):
        """
        Ensure we can update fields of AdviserUser
        """
        updated_user = AdviserUser.update(10, avatar="new_avatar.jpg")
        self.assertEqual(updated_user.avatar, AdviserUser.objects.get(id=10).avatar)
