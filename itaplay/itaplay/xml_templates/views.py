"""Module that represents views for xml templates"""
import json

from django.http import HttpResponse
from django.views.generic.base import View
from django.forms.models import model_to_dict

from xml_templates.models import XmlTemplate


class TemplateView(View):
    """View used for handling template."""

    def get(self, request, template_id=None):
        """Handling GET method.

        Args:
            request: Request to View.
            template_id: id of retrieved template.
        Returns:
            if template_id is None returns all templates.
            otherwise returns single template by given template_id.
        """
        if not template_id:
            xml_templates = XmlTemplate.get_all()
            data = [model_to_dict(i) for i in xml_templates]
            return HttpResponse(json.dumps(data))
        xml_template = XmlTemplate.get_by_id(template_id)
        data = model_to_dict(xml_template)
        return HttpResponse(json.dumps(data))

    def post(self, request):
        """Handling POST method.

        Args:
            request: Request to View.
        Returns:
            HttpResponse with code 201 if company is added.
        """
        template_name = request.POST.get('templateName')
        xml_file = request.FILES['file'].read()
        xml_template = XmlTemplate()
        xml_template.set(template_name, xml_file)
        xml_template.save()
        return HttpResponse(status=201)

    def delete(self, template_id):
        """Handling DELETE method.

        Args:
            template_id: id of deleted template.
        Returns:
            HttpResponse with code 201 if template is deleted.
        """
        XmlTemplate.delete(template_id)
        return HttpResponse(status=204)
