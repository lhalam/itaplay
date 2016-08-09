from django.shortcuts import render
from django.utils import timezone

from forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

from . import models


def closeInvitation(invitation):
    invitation.is_active = False
    invitation.usedTime = timezone.now()
    invitation.save()

def getInvitation(verification_code):
    if models.AdviserInvitations.objects.filter(verification_code=verification_code).exists():
        invitation = models.AdviserInvitations.objects.get(verification_code=verification_code)

        if not invitation.is_active:
            raise IndexError("Invitation is already used")
    else:
        raise IndexError("No open invitation")
    return invitation


def register(request):
    verification_code = request.GET.get('code', u"")

    if verification_code:
        try:
            invitation = getInvitation(verification_code)
        except IndexError as e:
            return HttpResponseBadRequest(e.message)
    else:
        return HttpResponseBadRequest("Invalid code")

    if request.method == 'POST':
        baseForm = UserForm(request.POST)

        if not baseForm.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")

        newBaseUser = baseForm.save(commit=False)
        newBaseUser.username = invitation.email
        newBaseUser.email = invitation.email
        newBaseUser.save()

        newExtendedUser = models.AdviserUser()
        newExtendedUser.setUpUser(newBaseUser, invitation)
        newExtendedUser.save()

        closeInvitation(invitation)

        return HttpResponseRedirect("/")

    else:
        baseForm = UserForm()

    return render(request, "register.html", {
        'baseForm': baseForm
    })
