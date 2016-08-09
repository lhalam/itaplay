from django.shortcuts import render
from django.utils import timezone

from forms import UserForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View

from . import models

def validate_verification_code(func):
    def wrapper(self, request, *args, **kwargs):
        verification_code = request.GET.get("code", "")

        if verification_code:
            if models.AdviserInvitations.objects.filter(verification_code=verification_code).exists():
                invitation = models.AdviserInvitations.objects.get(verification_code=verification_code)

                if not invitation.is_active:
                    return HttpResponseBadRequest("Invitation is already used")
            else:
                return HttpResponseBadRequest("No open invitation")
        else:
            return HttpResponseBadRequest("Invalid code")
        return func(self, request, *args, **kwargs)
    return wrapper


class RegistrationView(View):

    def close_invitation(self, invitation):
        invitation.is_active = False
        invitation.used_time = timezone.now()
        invitation.save()

    def get_invitation(self, verification_code):
        if models.AdviserInvitations.objects.filter(verification_code=verification_code).exists():
            invitation = models.AdviserInvitations.objects.get(verification_code=verification_code)

            if not invitation.is_active:
                raise IndexError("Invitation is already used")
        else:
            raise IndexError("No open invitation")
        return invitation

    @validate_verification_code
    def get(self, request):
        return render(request, "register.html")

    @validate_verification_code
    def post(self, request):
        verification_code = request.GET.get("code", "")

        invitation = self.get_invitation(verification_code)

        base_form = UserForm(request.POST)

        if not base_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")

        new_base_user = base_form.save(commit=False)
        new_base_user.username = invitation.email
        new_base_user.email = invitation.email
        new_base_user.save()

        new_extended_user = models.AdviserUser()
        new_extended_user.setup_user(new_base_user, invitation)
        new_extended_user.save()

        self.close_invitation(invitation)

        return HttpResponse(status=201)