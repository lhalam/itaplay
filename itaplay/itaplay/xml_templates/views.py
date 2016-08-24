from django.core import serializers
from django.views.generic.base import View
from .models import XmlTemplate
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json

# class TemplateView(View):
#     """
#     View for handing template
#     """

#     def get(self, request, template_id=None):
#         # xml_templates = XmlTemplate.get_xml_templates_list()
#         # data = serializers.serialize('json', xml_templates)
#         xml_templates = XmlTemplate.get_xml_templates_list()
#         data = serializers.serialize('json', xml_templates)
#         return HttpResponse(data, content_type='application/json')


class TemplateView(View):

    def get(self, request, template_id=None):
        # def xml_templates_list(self, request):
        """
        Handling GET method.
        param request: Request to View.
        return list of the companies
        """
        if not template_id:
            xml_templates = XmlTemplate.get_all()
            print xml_templates
            data2 = [model_to_dict(i) for i in xml_templates]
            print data2
            # data = serializers.serialize('json', xml_templates)
            # return HttpResponse(data, content_type='application/json')
            return HttpResponse(json.dumps(data2))
        xml_template = XmlTemplate.get_by_id(template_id)
        print xml_template
        data2 = model_to_dict(xml_template)
        print data2
        return HttpResponse(json.dumps(data2))
        # data = serializers.serialize('json', xml_template)
        # return HttpResponse(data, content_type='application/json')

    def post(self, request):
        """
        Handling POST method.
        param request: Request to View.
        return HttpResponse with code 201 if company is added
        """
        if request.method == 'POST':
            template_name = request.POST.get('templateName')
            xml_file = request.FILES['file'].read()
            obj = XmlTemplate()
            obj.set(template_name, xml_file)
            obj.save()
        return HttpResponse(201)

    def delete(self, request, template_id):
        """
        Handling DELETE method.
        args
            request: Request to View.
            pk: id of deleted template.
        return HttpResponse with code 201 if template is deleted.
        """

        if request.method == 'DELETE':
            print request
            print 'in delete'
            XmlTemplate.delete(template_id)
        print 'delete template'
        return HttpResponse(201)
