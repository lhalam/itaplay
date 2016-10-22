"""Module for creating invite links and sending e-mails"""
import uuid
from django.utils import timezone
from django.template import Context
from django.core.mail import EmailMessage
from django.template.loader import get_template
from authentication.models import AdviserInvitations
from company.models import Company
from itaplay.settings import EMAIL_SETTINGS


class InviteLinkGenerator(object):
    """Class for generating user invitation link

    Attributes :
        company_id (int): ID for company, who invite user
        email (str): user email, that would be stored in database
    """

    def __init__(self, company_id, email):
        self.company_id = company_id
        self.email = email

    def generate_link(self):
        """Function that generates user invitation link

        Returns :
            str :user invitation link
        """
        u_id = uuid.uuid4().hex  # u_id stores random generated hash
        AdviserInvitations.create(email=self.email,
                                  id_company=Company.get_company(self.company_id),
                                  verification_code=u_id,
                                  creation_time=timezone.now())
        return EMAIL_SETTINGS['URL_REGISTRATION'] + u_id


class EmailSender(object):
    """Class for sending emails

    Attributes :
        email (str): email which will be sent a letter
    """

    def __init__(self, email):
        self.email = email

    def send_invite(self, company_id):
        """Function that generates user invitation link

        Args:
            company_id (int): ID for company, who invite user
        Returns :
            True if success, False otherwise
        """
        plaintext = get_template('email_template.txt')
        invite_link = InviteLinkGenerator(company_id, self.email).generate_link()
        subject = "Invite to our service"
        body = plaintext.render(Context({'inviteLink': invite_link}))  # render template with data
        email = EmailMessage(subject, body, to=[self.email])
        return email.send() == 1
