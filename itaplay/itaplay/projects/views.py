import json
from xml.etree import ElementTree

from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.response import Response
from rest_framework import status, generics

from projects.serializers import AdviserProjectSerializer

from player.models import Player
from company.models import Company
from projects.models import AdviserProject
from xml_templates.models import XmlTemplate

class AdviserProjectView(View):
    """
    View for adding templates with clips to project template
    """

    def post(self, request):
        """
        Handling POST method.
        :param request: Request to View.
        :return: Http response with status code 201
        """
        data = json.loads(request.body)
        template = XmlTemplate.get_by_id(data['template_id']).template_content
        tree = ElementTree.fromstring(template)
        for area in data['areas']:
            template_area = tree.find(".//area[@id=\"%s\"]"%(area['id']))
            for clip in area['clips']:
                clip_tag = ElementTree.SubElement(template_area, 'clip')
                clip_tag.set('id',str(clip['pk']))
                clip_tag.set('src', clip['fields']['url'])
                clip_tag.set('mimetype', clip['fields']['mimetype'])
                clip_tag.text = clip['fields']['name']
        result_template = ElementTree.tostring(tree,encoding="us-ascii", method="xml")
        project = AdviserProject.objects.filter(id = data['project_id']).first()
        project.project_template = result_template
        project.save()
        return HttpResponse(status=201)


class AdviserProjectList(generics.ListCreateAPIView):
    """
    List all AdviserProjects of create new AdviserProject
    """

    serializer_class = AdviserProjectSerializer

    def get_queryset(self):
        """
        Filtering API only for users company
        :return: filtered queryset
        """
        user = self.request.user
        if user.is_superuser:
            return AdviserProject.objects.all()
        return AdviserProject.objects.filter(id_company=user.adviseruser.id_company)

    def post(self, request, *args, **kwargs):
        if not request.user.adviseruser.id_company_id:  # special for Admins
            return Response(status=status.HTTP_400_BAD_REQUEST)
        request.data["id_company"] = request.user.adviseruser.id_company_id
        project = AdviserProject.objects.get(id=self.create(request, *args, **kwargs).data["id"])
        if (request.data.get("players")):
            for obj in request.data.get("players"):
                player = Player.get_by_id(obj["id"])
                player.project = project 
                player.save()  
        return HttpResponse(status=201)


class AdviserProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a AdviserProject instance.
    """
    serializer_class = AdviserProjectSerializer

    def get_queryset(self):
        """
        Filtering API only for users company
        :return: filtered queryset
        """
        user = self.request.user
        if user.is_superuser:
            return AdviserProject.objects.all()
        return AdviserProject.objects.filter(id_company=user.adviseruser.id_company)


class AdviserProjectToPlayers(View):
    """
    Class-based view used for handling adding project to players while edditing.
    """
    def get(self, request, project_id):
        """
        Handling GET method.
        :param request: Request to View.
        :param project_id: id of project for which players will be returned
        :return: Http response with list of players that have current project
        """
        project = AdviserProject.objects.get(id=project_id)
        if project.id_company.id != request.user.adviseruser.id_company.id:
            return HttpResponseBadRequest("Permission denied")
        players = Player.objects.filter(project=project_id)
        data = [model_to_dict(i) for i in players]
        return HttpResponse(json.dumps(data))
        
    def put(self, request):
        """
        Handling PUT method. Send project to chosen players.
        :param request: Request to View.
        :return: Http response with status code 400 if players weren`t added. Http response with status code 201 if project is sended.
        """
        data = json.loads(request.body)
        if (not data.get("players")):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        project = AdviserProject.objects.get(id = data.get("project")["id"])
        if project.id_company.id != request.user.adviseruser.id_company.id:
            return HttpResponseBadRequest("Permission denied")
        for obj in data.get("players"):
            player = Player.get_by_id(obj["id"])
            player.project = project 
            player.save()  
        return HttpResponse(status=201)
