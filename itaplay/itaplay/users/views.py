from django.shortcuts import render
from django.contrib.auth.models import User
from authentication.models import AdviserUser
from django.views.generic import View
from django.http import HttpResponseBadRequest, HttpResponse
from django.forms.models import model_to_dict
import json
from django.core import serializers
# Create your views here.


class UserView(View):

    def get(self, request):
        user = request.user
        if user.is_superuser:
            users = AdviserUser.objects.all()
            data = serializers.serialize('json', users)
            return HttpResponse(data)
