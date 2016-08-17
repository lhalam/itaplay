import json
from models import Player
from forms import PlayerForm
from django.core import serializers
from django.core.context_processors import csrf

from django.forms.models import model_to_dict

from django.views.generic.base import View
from django.views.generic import DeleteView
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse


class PlayerView(View):
    def get(self, request, pk=None):
        if pk==None:
            data = serializers.serialize("json", Player.get_player())
            return HttpResponse(data)
        player = Player.get_player(pk)
        player = model_to_dict(player)
        return HttpResponse(json.dumps({"player":player}))

    def post(self, request):
        player = Player()
        data = json.loads(request.body)
        player_form = PlayerForm(data)
        if not player_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")
        player.set_player(json.loads(request.body)) 
        return HttpResponse(status=201)
      

class DeletePlayer(DeleteView):
    model = Player
    success_url = "/player"
           
