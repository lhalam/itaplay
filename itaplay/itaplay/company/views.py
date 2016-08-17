import json
from models import Company
from forms import CompanyForm
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
        data = json.loads(request.body)
        company_form = CompanyForm(data)
        if not company_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")
        company.set_company(json.loads(request.body)) 
        return HttpResponse(status=201)
      

class DeleteCompany(DeleteView):
    model = Company
    success_url = "/company"
           