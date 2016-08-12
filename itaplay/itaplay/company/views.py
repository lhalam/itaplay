import json
from models import Company
from django.core import serializers
from django.core.context_processors import csrf

from django.forms.models import model_to_dict

from django.views.generic.base import View
from django.views.generic import DeleteView
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse


class CompanyView(View):
    def get(self, request, pk=None):
        if pk==None:
            data = serializers.serialize("json", Company.get_company())
            return HttpResponse(data)
        company = Company.get_company(pk)
        company = model_to_dict(company)
        return HttpResponse(json.dumps({"company":company}))

    def post(self, request):
        company = Company()
        company.set_company(json.loads(request.body)) 
        name = "sent"
        return HttpResponseRedirect(json.dumps({"name" : name}))

class DeleteCompany(DeleteView):
    model = Company
           


