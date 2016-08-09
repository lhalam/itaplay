from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from . import models
from django.contrib.auth.views import login
import json


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

@login_required()
def login(request):
    if request.method == "POST":
        username = json.loads(request.body).get('username')
        password = json.loads(request.body).get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return HttpResponse("incorect username or password", status = 401)
    else:
        return HttpResponse(status = 400)


@login_required()
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required()
def custom_login(request):
    if request.method == "GET":
        print "GET"
        return render(request, 'login.html')
    else:
        print "not GET"
        return login(request)
