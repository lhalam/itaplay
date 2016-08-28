import json
from models import AdviserProject
from xml_templates.models import XmlTemplate
from clips.models import Clip
from xml.etree import ElementTree as ET

from django.core import serializers
from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.http import HttpResponse


class AdviserProjectView(View):
    """docs goes here"""

    def post(self, request):
        """
        Handling POST method.
        :param request: Request to View.
        :return: HttpResponse with code 201 if company is added or
        HttpResponseBadRequest if request contain incorrect data.
        """
        data = json.loads(request.body)
        template = XmlTemplate.get_by_id(data['template_id']).template_content
        root = ET.fromstring(template)
        for area in root.findall('area'):
            area_id = int(area.get('id'))-1
            clipTag = ET.SubElement(area, 'clip')
            clipTag.set('clip_id',str(data['areas'][area_id]['clip_id']))
            clip = Clip.objects.get(pk = data['areas'][area_id]['clip_id'])
            clipTag.set('src',str(clip.video))
            clipTag.text = clip.name
        result_template = ET.dump(root)
        print result_template
        return HttpResponse(status=201)



