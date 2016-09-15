import json
from models import Company
from authentication.models import AdviserUser
from django.contrib.auth.models import User
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
        user = AdviserUser.objects.get(user=request.user.id)
        company = []
        AdviserUser.is_admin = lambda self: False
        if user.is_admin():
            company = [model_to_dict(i) for i in Company.get_company()]
        else:
            company = Company.get_company(user.id_company.id)
            company = model_to_dict(company)
        print (json.dumps(company))
        return HttpResponse(json.dumps(company))





        


        user = AdviserUser.objects.get(user=request.user.id)
        company_id = int(company_id)
        print type(company_id), type(user.id_company.id) 
        if not company_id:
            data = serializers.serialize("json", Company.objects.filter(id=user.id_company.id))
            return HttpResponse(data)

        elif company_id != user.id_company.id:
            return HttpResponseBadRequest("Permission denied")
        else:
            company = Company.get_company(company_id)
            company = model_to_dict(company)
            users = AdviserUser.objects.filter(id_company=company_id)
            users = [model_to_dict(i) for i in users]
            data = {}
            data["company"] = company
            data["users"] = users
            return HttpResponse(json.dumps(data))

    def post(self, request):
        """
        Handling POST method.
        :param request: Request to View.
        :return: HttpResponse with code 201 if company is added or
        HttpResponseBadRequest if request contain incorrect data.
        """
        company = Company()
        data = json.loads(request.body)
        if data.get("administrator"):  
            data["administrator"]=AdviserUser.objects.get(id=data["administrator"])
        company_form = CompanyForm(data)
        if not company_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")
        company.set_company(data) 
        return HttpResponse(status=201)
    
    def put(self, request):
        """
        Handling put method.
        :param request: Request to View.
        :return: HttpResponse with code 201 if company is updated or
        HttpResponseBadRequest if request contain incorrect data.
        """
        data = json.loads(request.body)
        data["administrator"]=AdviserUser.objects.get(id=data["administrator"].get("id"))
        company = Company.get_company(data["id"]) 
        company_form = CompanyForm(data, company)
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
        data = serializers.serialize("json", Company.get_company())
        return HttpResponse(data)
      



           