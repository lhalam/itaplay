import json
from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from player.models import Player
from projects.models import AdviserProject
from django.http import HttpResponse

class GetMonitorView(View):
    def get(self, request):
        return render_to_response('monitor.html')

class MonitorView(View):    
    def get(self, request, mac):
        player = Player.objects.get(mac_address=mac)
        project = player.project
        template = project.project_template
        return HttpResponse(json.dumps({"template" : template}))
   