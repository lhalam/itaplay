from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from .forms import ClipForm
from .models import Clip


def list(request):
    if request.method=='POST':
        form = ClipForm(request.POST, request.FILES)
        if form.is_valid:
            newclip = Clip(video = request.FILES['uploadFromPC'])
            newclip.save()

            return HttpResponseRedirect(reverse('clips.views.list'))

    else:
        form = ClipForm()

    clips = Clip.objects.all()

    return render_to_response('list.html', {'clips': clips, 'form':form},
        context_instance=RequestContext(request))
        

