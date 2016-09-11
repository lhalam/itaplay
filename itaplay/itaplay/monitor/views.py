from django.shortcuts import render_to_response
from django.views.generic.base import View


class GetMonitorView(View):
    def get(self, request):
        return render_to_response('monitor.html')

