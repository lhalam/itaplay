import json
from models import Company
from authentication.models import AdviserUser

from forms import CompanyForm
from django.core import serializers
from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.http import HttpResponseBadRequest, HttpResponse


class CompanyView(View):
    """
    View used for handling company account.
    """
    def get(self, request, company_id=None):
        """
        Handling GET method.
        :args
            request: Request to View.
            company_id: id of company to be returned.
        :return: HttpResponse with company fields and values by id. 
        If company_id is 'None' returns all companies with their fields and values.
        """
        if not company_id:
            data = serializers.serialize("json", Company.get_company())
            return HttpResponse(data)
        company = Company.get_company(company_id)
        company = model_to_dict(company)
        return HttpResponse(json.dumps({"company":company}))

    def post(self, request):
        """
        Handling POST method.
        :param request: Request to View.
        :return: HttpResponse with code 201 if company is added or
        HttpResponseBadRequest if request contain incorrect data.
        """
        company = Company()
        data = json.loads(request.body)
        data["administrator"]=AdviserUser.objects.get(id=data["administrator"])
        company_form = CompanyForm(data)
        if not company_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")
        company.set_company(data) 
        return HttpResponse(status=201)

    def delete(self, request, company_id):
        """
        Handling DELETE method.
        args
            request: Request to View.
            company_id: id of company to be deleted.
        :return: HttpResponse with code 201 if company is deleted.
        """
        company = Company()
        company.delete_company(company_id)
        return HttpResponse(status=201)



           