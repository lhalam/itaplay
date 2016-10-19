import json

from models import Company
from forms import CompanyForm
from authentication.models import AdviserUser

from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.http import HttpResponseBadRequest, HttpResponse


def check_superadmin(func):
    def wrapper(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseBadRequest("Permission denied")
        return func(self, request, *args, **kwargs)             
    return wrapper        

class CompanyListView(View):
    """
    View used for handling company account.
    """

    def get(self, request):
        """
        Handling GET method.
        :param request:
        :return: HttpResponse with company fields and values by id_company of user which is logined.
        If user is superuser returns all companies with their fields and values.
        """
        if request.user.is_superuser:
            company = [model_to_dict(company) for company in Company.get_company()]
            return HttpResponse(json.dumps(company))
        adviser_user = request.user.adviseruser
        company = [model_to_dict(company) for company in Company.objects.filter(id=adviser_user.id_company.id)]
        return HttpResponse(json.dumps(company))
    
    @check_superadmin
    def post(self, request):
        """
        Handling POST method.
        :param request: Request to View.
        :return: HttpResponse with code 201 if company is added or
        HttpResponseBadRequest if request contain incorrect data or user is not superuser.
        """
        company = Company()
        data = json.loads(request.body)
        company_form = CompanyForm(data)
        if not company_form.is_valid():
            return HttpResponseBadRequest(str(company_form.errors))
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
        If user is not superuser and tries to get acces into foreign company
        returns HttpResponseBadRequest with 'Permission denied' massage.
        """
        company_id = int(company_id)
        if (not request.user.is_superuser) and (company_id != request.user.adviseruser.id_company.id):
            return HttpResponseBadRequest("Permission denied")
        data = { "company" : model_to_dict(Company.get_company(company_id)),
                  "users"  : Company.get_company(company_id).get_users()}
        return HttpResponse(json.dumps(data))
    
    def put(self, request, company_id):
        """
        Handling put method.
        :args
            request: Request to View.
            company_id: id of company to be updated.
        :return: HttpResponse with code 201 if company is updated or
        HttpResponseBadRequest if request contain incorrect data also if user is not superuser .
        """ 
        if (not request.user.is_superuser) and (Company.get_company(company_id).administrator != request.user.adviseruser):
            return HttpResponseBadRequest("Permission denied")
        data = json.loads(request.body)
        if data.get("administrator"):
            data["administrator"] = AdviserUser.objects.get(id=data.get("administrator").get("id"))
        company = Company.get_company(data["id"]) 
        company_form = CompanyForm(data, company)
        if not company_form.is_valid():
            return HttpResponseBadRequest(str(company_form.errors))
        company.set_company(data) 
        return HttpResponse(status=201)    

    @check_superadmin
    def delete(self, request, company_id):
        """
        Handling DELETE method.
        args
            request: Request to View.
            company_id: id of company to be deleted.
        :return: HttpResponse with code 201 if company is deleted.
        HttpResponseBadRequest with 'Permission denied' if user is not superuser.
        """
        Company().delete_company(company_id)
        return HttpResponse(status=201)
