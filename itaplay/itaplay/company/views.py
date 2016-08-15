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
    """
    View used for handling company account.
    """
    def get(self, request, pk=None):
        """
        Handling GET method.
        :args
            request: Request to View.
            pk: id of company to by returned.
        :return: HttpResponse with company fields and values by id. 
        If pk is 'None' returns all companies with their fields and values
        """
        if pk==None:
            data = serializers.serialize("json", Company.get_company())
            return HttpResponse(data)
        company = Company.get_company(pk)
        company = model_to_dict(company)
        return HttpResponse(json.dumps({"company":company}))

    def post(self, request):
        """
        Handling POST method.
        :param request: Request to View.
        :return: HttpResponse with code 201 if company is added or
        HttpResponseBadRequest if request contain incorrect data
        """
        company = Company()
        data = json.loads(request.body)
        company_form = CompanyForm(data)
        if not company_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")
        company.set_company(json.loads(request.body)) 
        return HttpResponse(status=201)
      

class DeleteCompany(DeleteView):
    """
    Class for deleteing company object, based on DeleteView class. 
    Deletes company by id and redirects to the success URL.
    """
    model = Company
    success_url = "/company"
           