from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class MonitorView(View):
    def get(self, request):
        return render_to_response('monitor.html')
