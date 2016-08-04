from django.shortcuts import render

from forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse

from . import models


def register(request):
    verificationCode = request.GET.get('code', u"") # maybe should move validation functionality to another function
    if not verificationCode:
        return HttpResponse("Invalid code")

    if models.AdviserInvitations.objects.filter(verification_code=verificationCode).exists():
        invitation = models.AdviserInvitations.objects.get(verification_code = verificationCode)

        if invitation.is_active == True:
            return HttpResponse("User already registered")
    else:
        return HttpResponse("Invalid code")


    if request.method == 'POST':
        baseForm = UserForm(request.POST)

        if baseForm.is_valid():
            newBaseUser = baseForm.save(commit=False)
            newBaseUser.username = invitation.email
            newBaseUser.email = invitation.email
            newBaseUser.save()

            newExtendedUser = models.AdviserUser()
            newExtendedUser.user = newBaseUser
            newExtendedUser.avatar = "default-user-logo.png" # or should make default value on DB
            newExtendedUser.ID_company = invitation.ID_company
            newExtendedUser.save()

            invitation.is_active = True
            invitation.save()

            return HttpResponseRedirect("/")

    else:
        baseForm = UserForm()

    return render(request, "register.html", {
        'baseForm': baseForm
    })
