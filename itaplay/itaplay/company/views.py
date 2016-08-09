import json
from models import Company
from django.views.generic.base import View
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse


def company_get(request):
    company = [ { "id" : i.id,
                "company_logo": i.company_logo,
                "company_name": i.company_name,
                "company_mail": i.company_mail,
                "company_phone": i.company_phone,
                "company_address": i.company_address,}
            for i in Company.objects.all()]
    return HttpResponse(json.dumps({"company" : company} , ensure_ascii=False))

def company_post(request):
    company = Company(company_logo = json.loads(request.body).get("company_logo"), 
                      company_name= json.loads(request.body).get("company_name"), 
                      company_mail= json.loads(request.body).get("company_mail"), 
                      company_phone= json.loads(request.body).get("company_phone"), 
                      company_address= json.loads(request.body).get("company_address"),)
    
    company.save()
    return HttpResponseRedirect('/')
    