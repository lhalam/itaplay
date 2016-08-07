import uuid
from authentication.models import AdviserInvitations
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context

URL_REGISTRATION = "http://mysite.com/auth/register?code="


class InviteLinkGenerator(object):
    def __init__(self, company_id, email):
        self.companyId = company_id
        self.email = email

    def generate_link(self):
        uID = uuid.uuid4().hex
        newUser = AdviserInvitations(email=self.email,
                                     IdCompany=self.companyId,
                                     verificationCode=uID,
                                     isActive=True,
                                     creationTime=timezone.now(),
                                     usedTime=timezone.now())
        newUser.save()
        return URL_REGISTRATION + uID


class EmailSender(object):
    def __init__(self, email):
        self.email = email

    def send_invite(self, company_id):
        plaintext = get_template('email_template.txt')
        inviteLink = InviteLinkGenerator(company_id, self.email).generate_link()
        subject = "Invite to our service"
        body = plaintext.render(Context({'inviteLink': inviteLink}))
        email = EmailMessage(subject, body, to=[self.email])
        email.send()
