from django.core import serializers
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect, \
    get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from forms import ClipForm
from models import Clip


def list(request):
    """
    Handling GET method for all clips.
    
    :return: all clips
    """    
    clips = Clip()
    clips = clips.get_all_clips()
    data = serializers.serialize('json', clips)

    return HttpResponse(data, content_type='application/json')


def get_clip(request, pk):
    """
    Handling GET method for one clip.
    
    :return: clip pk
    """

    clip = Clip()
    clip = clip.get_clip(pk)

    data = serializers.serialize('json', clip)

    return HttpResponse(data, content_type='application/json')


def clip_delete(request, pk):
    """
    Handling DELETE method.
    
    :return: HttpResponse with code 201 if clip is deleted.
    """

    clip = Clip()
    if request.method == 'DELETE':
        clip.delete_clip(pk)
    
    return HttpResponse(status=201)

def post(request):
    """
    Handling POST method.
    
    :return: HttpResponse with code 201 if clip is added.
    """

    if request.method == 'POST':
        form = ClipForm(request.POST, request.FILES)
        if form.is_valid:
            newclip = Clip(video=request.FILES['file'],
                           name=request.POST['filename'])
            newclip.save_clip()
            return HttpResponse(status=201)
    else:
        form = ClipForm()

    return HttpResponse(status=201)


