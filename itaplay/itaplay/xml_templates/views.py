import json
from django.core import serializers
from django.shortcuts import render
from .models import XmlTemplate
from django.http import HttpResponse


# Create your views here.
def xml_templates_list(request):
    xml_templates = XmlTemplate.objects.all()
    data = serializers.serialize('json', xml_templates)
    return HttpResponse(data, content_type='application/json')


def xml_templates_add(request):
    if request.method == 'POST':
        # print request.body
        template_name = request.POST.get('templateName')
        # print template_name
        xml_file = request.FILES['file'].read()
        # print xml_file
        xml_template_obj = XmlTemplate(template_name=template_name,
            template_content = xml_file)
        # print xml_template_obj
        xml_template_obj.save()

    # print 'add template'
    return HttpResponse(200)


def xml_template_delete(request, pk):
    # xml_template = XmlTemplate()
    if request.method == 'DELETE':
        XmlTemplate.objects.filter(pk=pk).delete()
        print request.body
    print('delete template')
    return HttpResponse(200)
