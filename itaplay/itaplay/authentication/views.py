from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib import auth
from forms import UserForm
from . import models
import json

from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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


class LoginView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)


    def post(self, request):
        data = json.loads(request.body)

        username = data.get('username', None)
        password = data.get('password', None)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            return HttpResponse("incorect username or password", status=401)

        #else:
        return HttpResponse(status=400)


    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')




