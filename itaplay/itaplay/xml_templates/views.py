import json
from .models import XmlTemplate
from django.http import HttpResponse
from django.views.generic.base import View
from django.forms.models import model_to_dict


class TemplateView(View):

    def get(self, request, template_id=None):
        """
        Handling GET method.
        param request: Request to View.
        return list of the companies
        """
        if not template_id:
            xml_templates = XmlTemplate.get_all()
            data = [model_to_dict(i) for i in xml_templates]
            return HttpResponse(json.dumps(data))
        xml_template = XmlTemplate.get_by_id(template_id)
        data = model_to_dict(xml_template)
        return HttpResponse(json.dumps(data))

    def post(self, request):
        """
        Handling POST method.
        param request: Request to View.
        return HttpResponse with code 201 if company is added
        """
        if request.method == 'POST':
            template_name = request.POST.get('templateName')
            xml_file = request.FILES['file'].read()
            xml_template = XmlTemplate()
            xml_template.set(template_name, xml_file)
            xml_template.save()
        return HttpResponse(201)

    def delete(self, request, template_id):
        """
        Handling DELETE method.
        args
            request: Request to View.
            template_id: id of deleted template.
        return HttpResponse with code 201 if template is deleted.
        """
        if request.method == 'DELETE':
            XmlTemplate.delete(template_id)
        return HttpResponse(201)
