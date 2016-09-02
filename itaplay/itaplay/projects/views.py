import json
from xml.etree import ElementTree as ET

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
            clipTag = ET.SubElement(area, 'clip')
            clipTag.set('clip_id',str(data['areas'][area_id]['clip_id']))
            clip = Clip.objects.get(pk = data['areas'][area_id]['clip_id'])
            clipTag.set('src',str(clip.video))
            clipTag.text = clip.name
        result_template = ET.dump(root)
        print result_template
        return HttpResponse(status=201)

    def get(self, request, project_id=None):
        """
        Handling get request
        :param request:
        :param project_id:
        :return:
        """
        if not project_id:
            data = serializers.serialize("json", AdviserProject.objects.all())   # TODO limit amount of objects
            return HttpResponse(data)
        adviser_project = AdviserProject.objects.filter(id=int(project_id))     # TODO Check for id correctness
        if not adviser_project.exists():
            return HttpResponseBadRequest
        data = json.dumps(model_to_dict(adviser_project.first()))
        return HttpResponse(data)

    def put(self, request, project_id=None):

        return HttpResponse

    def delete(self, request, project_id=None):

        if not project_id:
            return HttpResponseBadRequest

        adviser_project = AdviserProject.objects.filter(id=project_id)  # TODO Check for id correctness

        if not adviser_project.exists():
            return HttpResponseBadRequest

        adviser_project.first().delete()  # TODO Improve code quality

        return HttpResponse


class AdviserProjectList(APIView):
    """
    List all snippets, or create a new AdviserProject.
    """
    def get(self, request, format=None):
        projects = AdviserProject.objects.all()
        serializer = AdviserProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdviserProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdviserProjectDetails(APIView):
    """
     Retrieve, update or delete a AdviserProject instance.
     """
    def get_object(self, pk):
        try:
            return AdviserProject.objects.get(pk=pk)
        except AdviserProject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = AdviserProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = AdviserProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
