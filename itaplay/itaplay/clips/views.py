from django.core import serializers
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect, \
    get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from forms import ClipForm
from models import Clip
from django.views.generic import View
import itaplay.s3utils

class ClipView(View):
    """
    Handling POST method.
    
    :return: HttpResponse with code 201 if clip is added.
    """
    def post(self, request, *args, **kwargs):
        form = ClipForm(request.POST, request.FILES)
        if form.is_valid:
            newclip = Clip(video=request.FILES['file'],
                           name=request.POST['filename'],
                           description=request.POST['description'])
            newclip.save_clip()
            return HttpResponse(status=201)

    """
    Handling DELETE method.
    
    :return: HttpResponse with code 201 if clip is deleted.
    """
    def delete(self, request, clip_id):
        clip = Clip()
        clip.delete_clip(clip_id)
        return HttpResponse(status=201)
    """
    Handling GET method for all clips.
    
    :return: all clips
    """  
    def get(self, request, clip_id=None):
        if not clip_id:
            clips = Clip()
            clips = clips.get_all_clips()
            data = serializers.serialize('json', clips)
            return HttpResponse(data, content_type='application/json')

        clip = Clip()
        clip = clip.get_clip(clip_id)
        data = serializers.serialize('json', clip)
        return HttpResponse(data, content_type='application/json')

