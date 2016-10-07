from django.shortcuts import render
from django.contrib.auth.models import User
from authentication.models import AdviserUser, AdviserInvitations
from django.views.generic import View
from django.http import HttpResponseBadRequest, HttpResponse
from django.forms.models import model_to_dict
import json
from django.core import serializers

from rest_framework.response import Response
from rest_framework import status, generics

from users.serializers import AdviserUsersSerializer
# Create your views here.



class AdviserUsersList(generics.ListCreateAPIView):

    serializer_class = AdviserUsersSerializer

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return AdviserUser.objects.all()


class InvitationView(View):

    def get(self, request):
        user = request.user
        if user.is_superuser:
            invitations = AdviserInvitations.objects.all()
            data = serializers.serialize('json', invitations)
            return HttpResponse(data)

