from django.core import serializers
from django.template import RequestContext
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect, \
    get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from forms import ClipForm
from models import Clip


def list(request):
    if request.method == 'POST':
        form = ClipForm(request.POST, request.FILES)
        if form.is_valid:
            newclip = Clip(video=request.FILES['file'],
                           name=request.POST['filename'])
            newclip.save()
    else:
        form = ClipForm()

    clips = Clip.objects.all()
    data = serializers.serialize('json', clips)

    return HttpResponse(data, content_type='application/json')


def get_clip(request, pk):
    clip = Clip()
    clip = clip.get_clip(pk)

    data = serializers.serialize('json', clip)

    return HttpResponse(data, content_type='application/json')


def clip_delete(request, pk):
    clip = Clip()
    if request.method == 'DELETE':
        clip.delete_clip(pk)
    
    return HttpResponse(status=201)

