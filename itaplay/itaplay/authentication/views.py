from django.shortcuts import render

from forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

from . import models


def getInvitation(verificationCode):
    if models.AdviserInvitations.objects.filter(verification_code=verificationCode).exists():
        invitation = models.AdviserInvitations.objects.get(verification_code=verificationCode)

        if not invitation.is_active:
            raise IndexError("Invitation is already used")
    else:
        raise IndexError("No open invitation")
    return invitation


def register(request):
    verificationCode = request.GET.get('code', u"")

    if verificationCode:
        try:
            invitation = getInvitation(verificationCode)
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
        newBaseUser.setUpUser(newBaseUser, invitation)
        newExtendedUser.save()

        invitation.is_active = False
        invitation.save()

        return HttpResponseRedirect("/")

    else:
        baseForm = UserForm()

    return render(request, "register.html", {
        'baseForm': baseForm
    })
