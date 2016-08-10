import json
from models import Company
from django.views.generic.base import View
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse


def company_get(request):
    data = [ { "id" : i.id,
               "company_logo": i.company_logo,
               "company_name": i.company_name,
               "company_mail": i.company_mail,
               "company_phone": i.company_phone,
               "company_address": i.company_address,}
               for i in Company.objects.all()] 
    return HttpResponse(json.dumps({"company" : data}, ensure_ascii=False))

def company_post(request):
    company = Company(**json.loads(request.body))
    company.save()
    name = "posted"
    return HttpResponse({"name" : name})
    
def current_company(request, company_id):
    company = Company.objects.get(id = company_id)
    args ={"id":company.id, 
           "company_logo": company.company_logo,
           "company_name": company.company_name,
           "company_mail": company.company_mail,  
           "company_phone": company.company_phone, 
           "company_address": company.company_address}
    return HttpResponse(json.dumps({"current_company":args} , ensure_ascii=False))

def delete_company(request):
    company = Company.objects.get(id = json.loads(request.body).get("id"))
    company.delete()
    name = "deleted"
    return HttpResponse({"name" : name})

def edit_company(request):
    company = Company.objects.get(id = json.loads(request.body).get("id"))
    company = Company(**json.loads(request.body))
    company.save()
    name = "changed"
    return HttpResponse({"name" : name})