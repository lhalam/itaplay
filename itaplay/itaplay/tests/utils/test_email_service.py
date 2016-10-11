import mock
from django.test import TestCase
from django.core import mail
from utils import EmailService
from company.models import Company

class FakeObject(object):
    hex = "123456789"

def fakeReturnValue():
    return FakeObject()

class InviteLinkGenerator(TestCase):

    def setUp(self):
        company = Company.objects.create(
            id = 1,
            zipcode="79008",
            logo="http://test.test",
            name="testcompany",
            mail="test@test.test",
            phone="+380901234567",
        )
        company.save()

    @mock.patch('uuid.uuid4',fakeReturnValue)
    def test_generated_invite_link(self):
        generator = EmailService.InviteLinkGenerator(1, "mail@mail.com")
        generated_link = generator.generate_link()
        self.assertEqual(generated_link, "http://127.0.0.1:8000/auth/register?code=123456789")


class EmailSender(TestCase):

    def setUp(self):
        company = Company.objects.create(
            id = 1,
            zipcode="79008",
            logo="http://test.test",
            name="testcompany",
            mail="test@test.test",
            phone="+380901234567",
        )
        company.save()

    @mock.patch('utils.EmailService.InviteLinkGenerator.generate_link')
    def test_send_email(self, fake_generator):
        fake_generator.return_value = "http://127.0.0.1:8000/auth/register?code=93f4535193af489d87efc12fb8d89e01"
        assert_body = "Hello!\n\nWe are pleased to invite you to our service.\n\n" \
                      "To register, visit the link: http://127.0.0.1:8000/auth/register?code=93f4535193af489d87efc12fb8d89e01" \
                      "\n\nHave a nice day!"
        sender = EmailService.EmailSender("from@mail.com")
        return_value = sender.send_invite(1)

        self.assertEqual(return_value, True)
        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'Invite to our service')
        self.assertEqual(mail.outbox[0].body, assert_body)
