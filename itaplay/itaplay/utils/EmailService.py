import uuid
from authentication.models import AdviserInvitations
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context

URL_REGISTRATION = "http://127.0.0.1:8000/auth/register?code="


class InviteLinkGenerator(object):
    def __init__(self, company_id, email):
        self.company_id = company_id
        self.email = email

    def generate_link(self):
        u_id = uuid.uuid4().hex
        new_user = AdviserInvitations(email=self.email,
                                      id_company=self.company_id,
                                      verification_code=u_id,
                                      creation_time=timezone.now())
        new_user.save()
        return URL_REGISTRATION + u_id


class EmailSender(object):
    def __init__(self, email):
        self.email = email

    def send_invite(self, company_id):
        plaintext = get_template('email_template.txt')
        invite_link = InviteLinkGenerator(company_id, self.email).generate_link()
        subject = "Invite to our service"
        body = plaintext.render(Context({'inviteLink': invite_link}))
        email = EmailMessage(subject, body, to=[self.email])
        email.send()
