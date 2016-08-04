from django.shortcuts import render

from forms import UserForm
from django.http import HttpResponseRedirect

from . import models


def register(request):
    if request.method == 'POST':
        baseForm = UserForm(request.POST)

        if baseForm.is_valid():
            newBaseUser = baseForm.save(commit=False)
            newBaseUser.email = baseForm.data[u'username']
            newBaseUser.save()

            newExtendedUser = models.AdviserUser()
            newExtendedUser.user = newBaseUser
            newBaseUser.avatar = "static//img//default-user-logo.png" # replace with static path
                                                                      # or make default value on DB
            newExtendedUser.save()

            return HttpResponseRedirect("/")
    else:
        baseForm = UserForm()

    return render(request, "register.html", {
        'baseForm': baseForm
    })
