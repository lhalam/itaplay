from django.core import serializers
from django.views.generic.base import View
from .models import XmlTemplate
from django.http import HttpResponse


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

    def get(self, request, pk=None):
        # def xml_templates_list(self, request):
        """
        Handling GET method.
        param request: Request to View.
        return list of the companies
        """
        if not pk:
            xml_templates = XmlTemplate.get_xml_templates_list()
            data = serializers.serialize('json', xml_templates)
            return HttpResponse(data, content_type='application/json')
        xml_template = XmlTemplate.get_by_id(pk=pk)
        data = serializers.serialize('json', xml_template)
        return HttpResponse(data, content_type='application/json')

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
            obj.set_xml_template(template_name, xml_file)
            obj.save()
        return HttpResponse(201)

    def delete(self, request, pk):
        """
        Handling DELETE method.
        args
            request: Request to View.
            pk: id of deleted template.
        return HttpResponse with code 201 if template is deleted.
        """
        if request.method == 'DELETE':
            XmlTemplate.delete_xml_template(pk=pk)
        return HttpResponse(201)
