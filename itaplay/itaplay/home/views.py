from django.shortcuts import render, render_to_response
from django.views.generic.base import View
# Create your views here.


class IndexView(View):

    def get(self, request):
    	return render_to_response('index.html')