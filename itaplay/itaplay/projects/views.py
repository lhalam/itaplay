import json
from xml.etree import ElementTree as ET
from xml_templates.models import XmlTemplate

from projects.models import AdviserProject
from clips.models import Clip
from xml_templates.models import XmlTemplate

from django.core import serializers
from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from projects.serializers import AdviserProjectSerializer

from django.http import Http404

from company.models import Company


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
            for clip in data['areas'][area_id]['clips']:
                clipTag = ET.SubElement(area, 'clip')
                clipTag.set('id',str(clip['pk']))
                clipTag.set('src',clip['fields']['video'])
                clipTag.text = clip['fields']['name']
        result_template = ET.tostring(root,encoding="us-ascii", method="xml")
        print result_template
        return HttpResponse(status=201)


class AdviserProjectList(APIView):
    """
    List all snippets, or create a new AdviserProject.
    """
    def get(self, request, format=None):
        projects = AdviserProject.objects.all()
        serializer = AdviserProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if not request.user.adviseruser.id_company_id:  # special for Admins
            return Response(status=status.HTTP_400_BAD_REQUEST)
        request.data["id_company"] = request.user.adviseruser.id_company_id
        serializer = AdviserProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdviserProjectDetails(APIView):
    """
     Retrieve, update or delete a AdviserProject instance.
     """
    def get_object(self, id):
        try:
            return AdviserProject.objects.get(id=id)
        except AdviserProject.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        project = self.get_object(id)
        serializer = AdviserProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        project = self.get_object(id)
        serializer = AdviserProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        project = self.get_object(id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
