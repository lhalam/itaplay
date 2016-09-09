import json

from models import AdviserProject

from player.models import Player
from company.models import Company

from xml.etree import ElementTree as ET

from django.views.generic.base import View
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status, generics

from projects.serializers import AdviserProjectSerializer
from projects.models import AdviserProject
from xml_templates.models import XmlTemplate


class AdviserProjectView(View):
    """docs goes here"""

    def post(self, request):
        """
        Handling POST method.
        :param request: Request to View.
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
        project = AdviserProject.objects.filter(id = data['project_id']).first()
        project.project_template = result_template
        project.save()
        return HttpResponse(status=201)


class AdviserProjectList(generics.ListCreateAPIView):
    """
    List all AdviserProjects of create new AdviserProject
    """
    queryset = AdviserProject.objects.all()
    serializer_class = AdviserProjectSerializer

    def post(self, request, *args, **kwargs):
        if not request.user.adviseruser.id_company_id:  # special for Admins
            return Response(status=status.HTTP_400_BAD_REQUEST)
        request.data["id_company"] = request.user.adviseruser.id_company_id
        project = AdviserProject.objects.get(id=self.create(request, *args, **kwargs).data["id"])
        for obj in request.data.get("players"):
            player = Player.get_by_id(obj["id"])
            player.project = project 
            player.save()  
        return HttpResponse(status=201)


class AdviserProjectDetails(generics.RetrieveUpdateDestroyAPIView):

    '''
    Retrieve, update or delete a AdviserProject instance.
    '''

    queryset = AdviserProject.objects.all()
    serializer_class = AdviserProjectSerializer


class AdviserProjectToPlayers(View):
    def put(self, request):
        data = json.loads(request.body)
        project = AdviserProject.objects.get(id = data.get("project")["id"])
        for obj in data.get("players"):
            player = Player.get_by_id(obj["id"])
            player.project = project 
            player.save()  
        return HttpResponse(status=201)