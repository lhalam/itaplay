import json
from models import Company
from authentication.models import AdviserUser
from django.contrib.auth.models import User
from forms import CompanyForm
from django.core import serializers
from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.http import HttpResponseBadRequest, HttpResponse


class CompanyListView(View):
    """
    View used for handling company account.
    """

    def get(self, request):
        """
        Handling GET method.
        :args
            request: Request to View.
            company_id: id of company to be returned.
        :return: HttpResponse with company fields and values by id_company of user which is logined. 
        If user is super admin returns all companies with their fields and values.
        """
        user = request.user
        if user.is_superuser:
            company = [model_to_dict(i) for i in Company.get_company()]
            return HttpResponse(json.dumps(company))
        adviser_user = AdviserUser.objects.get(user=request.user.id)
        company = [model_to_dict(i) for i in Company.objects.filter(id=adviser_user.id_company.id)]
        return HttpResponse(json.dumps(company))     

    def post(self, request):
        """
        Handling POST method.
        :param request: Request to View.
        :return: HttpResponse with code 201 if company is added or
        HttpResponseBadRequest if request contain incorrect data.
        """
        if not request.user.is_superuser:
            return HttpResponseBadRequest("Permission denied")
        company = Company()
        data = json.loads(request.body)
        if data.get("administrator"):  
            data["administrator"]=AdviserUser.objects.get(id=data["administrator"])
        company_form = CompanyForm(data)
        if not company_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")
        company.set_company(data) 
        return HttpResponse(status=201)
    
    
      
class CompanyDetailsView(View):
    """
    View used for handling company account.
    """
    def get(self, request, company_id):
        """
        Handling GET method.
        :args
            request: Request to View.
            company_id: id of company to be returned.
        :return: HttpResponse with company fields and values by id. 
        If company_id is 'None' returns all companies with their fields and values.
        """

        company_id = int(company_id)  
        if (not request.user.is_superuser)  and  (company_id != AdviserUser.objects.get(user=request.user.id).id_company.id):
           return HttpResponseBadRequest("Permission denied")
        company = Company.get_company(company_id)
        company = model_to_dict(company)
        users = AdviserUser.objects.filter(id_company=company_id)
        users = [model_to_dict(i) for i in users]
        data = {}
        data["company"] = company
        data["users"] = users
        return HttpResponse(json.dumps(data))

    def put(self, request, company_id):
        """
        Handling put method.
        :param request: Request to View.
        ^company_id: id of company to be updated.
        :return: HttpResponse with code 201 if company is updated or
        HttpResponseBadRequest if request contain incorrect data.
        """
        if not request.user.is_superuser:
            return HttpResponseBadRequest("Permission denied")
        data = json.loads(request.body)
        if type(data.get("administrator"))==int: 
            data["administrator"]=AdviserUser.objects.get(id=data.get("administrator"))
        elif data.get("administrator"): 
            data["administrator"]=AdviserUser.objects.get(**data.get("administrator"))
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

        if not request.user.is_superuser:
            return HttpResponseBadRequest("Permission denied")
        company = Company()
        company.delete_company(company_id)
        return HttpResponse(status=201)