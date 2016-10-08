from django.shortcuts import render
from django.contrib.auth.models import User
from authentication.models import AdviserUser
from django.views.generic import View
from django.http import HttpResponseBadRequest, HttpResponse
from django.forms.models import model_to_dict
import json
import datetime
from django.core import serializers
# Create your views here.


class UserView(View):

    def datetime_handler(self, x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

    def get(self, request):
        user = request.user
        if not user.is_superuser:
            data = {}
            data['AdviserUser'] = model_to_dict(AdviserUser.objects.get(user_id=user.id))
            data['User'] = model_to_dict(User.objects.get(id=user.id))
            print 'here ',data
            return HttpResponse(json.dumps(data, default=self.datetime_handler))
