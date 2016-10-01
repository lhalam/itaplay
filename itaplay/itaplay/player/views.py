import json
from models import Player
from forms import PlayerForm
from projects.models import AdviserProject
from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest


class PlayerView(View):

    def get(self, request, player_id=None):
        if player_id==None:
            data = [model_to_dict(i) for i in Player.get_all()]
            return HttpResponse(json.dumps(data))
        player = Player.get_by_id(player_id)
        player = model_to_dict(player)
        return HttpResponse(json.dumps({"player": player}))

    def post(self, request):
        player = Player()
        data = json.loads(request.body)
        if data.get("project"):
            data["project"] = AdviserProject.objects.get(id=data["project"])
        player_form = PlayerForm(data)
        if not player_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")
        player.set(data) 
        return HttpResponse(status=201)
    
    def put(self, request):
        player = Player()
        data = json.loads(request.body)
        if data.get("project"):
            data["project"] = AdviserProject.objects.get(id=data["project"])
        player_form = PlayerForm(data)
        if not player_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")
        player.set(data) 
        return HttpResponse(status=201)

    def delete(self, request, player_id):
        Player.delete_by_id(player_id)
        return HttpResponse(200)
