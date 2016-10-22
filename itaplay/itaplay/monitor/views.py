"""
Views for monitor.
Handle GET and HAED methods.
"""
import json

from player.models import Player
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render_to_response


class GetMonitorView(View):
    """
    View used for return Monitor page.
    """
    def get(self, request):
        """
        Handling GET method.
        :param request: Request to View.
        :return: rendered Monitor page.
        """
        return render_to_response('monitor.html')

class MonitorView(View):
    """
    View used for handling Monitor.
    """
    def get(self, request, mac):
        """
        Handling GET method.
        :args
            request: Request to View.
            mac: mac-address of player.
        :return: HttpResponse with project's template and template's hashsum of player, 
        gotten by mac-address.
        """
        player = Player.objects.get(mac_address=mac)
        template = player.project.project_template
        hashsum = player.project.project_hash
        return HttpResponse(json.dumps({"template" : template, 'hashsum': hashsum}))

    def head(self, request, mac):
        """
        Handling HEAD method.
        :args
            request: Request to View.
            mac: mac-address of player.
        :return: last modified template's hash sum of player, gotten by mac-address.
        """

        player = Player.objects.get(mac_address=mac)
        if player.project:
            hashsum = player.project.project_hash
            response = HttpResponse('')
            response['Last-Modified'] = hashsum
            return response
        return HttpResponse(status=204)
