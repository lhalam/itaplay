from django.shortcuts import render, render_to_response
from django.views.generic.base import View
# Create your views here.


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get(self, request):
    	return render_to_response('index.html')