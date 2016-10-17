from django.shortcuts import render
from django.contrib.auth.models import User
from authentication.models import AdviserUser, AdviserInvitations
from django.views.generic import View
from django.http import HttpResponseBadRequest, HttpResponse
from django.forms.models import model_to_dict
import json
import datetime
from users.forms import UserForm
from django.core import serializers

from rest_framework.response import Response
from rest_framework import status, generics

from users.serializers import AdviserUsersSerializer, AdviserInvitationsSerializer
# Create your views here.


class UserView(View):

    def datetime_handler(self, x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

    def get(self, request):
        user = request.user
        data = {}
        if not user.is_superuser:
            data['AdviserUser'] = model_to_dict(AdviserUser.objects.get(user_id=user.id))
        data['User'] = model_to_dict(User.objects.get(id=user.id))
        return HttpResponse(json.dumps(data, default=self.datetime_handler))


    def put(self, request):
        data = json.loads(request.body)
        user_form = UserForm(data['User'])
        if not user_form.is_valid():
            return HttpResponseBadRequest('Invalid input data', status=400)
        adviser_user = AdviserUser.objects.get(id=data['AdviserUser']['id'])
        adviser_user.set_adviser_user(data['AdviserUser'])
        user = User.objects.get(id=data['User']['id'])
        user.last_name = data['User']['last_name']
        user.first_name = data['User']['first_name']
        user.save()
        return HttpResponse(status=201)


class AdviserUserDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = AdviserUsersSerializer

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return AdviserUser.objects.all()


class AdviserInvitationsList(generics.ListCreateAPIView):

    serializer_class = AdviserInvitationsSerializer

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return AdviserInvitations.objects.all()


class AdviserUsersList(generics.ListCreateAPIView):

    serializer_class = AdviserUsersSerializer

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return AdviserUser.objects.all()
        if not user.is_superuser:
            return AdviserUser.objects.filter(id_company=user.adviseruser.id_company)
