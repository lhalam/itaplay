from django.shortcuts import render

from forms import UserForm, AdviserUserForm
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        baseForm = UserForm(request.POST)
        extendedForm = AdviserUserForm(request.POST)
        if baseForm.is_valid() and extendedForm.is_valid():
            newBaseUser = baseForm.save(commit=False)
            newBaseUser.email = baseForm.data[u'username']
            newBaseUser.save()

            newExtendedUser = extendedForm.save(commit=False)
            newExtendedUser.user = newBaseUser
            newExtendedUser.save()

            return HttpResponseRedirect("/")
    else:
        baseForm = UserForm()
        extendedForm = AdviserUserForm()
    return render(request, "register.html", {
        'baseForm': baseForm,
        'extendedForm': extendedForm
    })