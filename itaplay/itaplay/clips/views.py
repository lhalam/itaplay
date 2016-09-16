from django.core import serializers
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from forms import ClipForm
from models import Clip
from django.views.generic import View
import json

# Class for clips

class ClipView(View):

    """
    Handling POST method.

    :return: HttpResponse with code 201 if clip is added.
    """

    def post(self, request):
        form = ClipForm(request.POST, request.FILES)

        if form.is_valid:
            newclip = Clip(name=request.POST['filename'],
                           description=request.POST['description'],
                           clipfile=request.FILES['file']
                           )
            newclip.save_on_amazon_with_boto()
            newclip.save()

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

    """
    Handling PUT method for current clip.
    
    :return: HttpResponse with code 201 if clip is updated.
    """

    def put(self, request, clip_id):

        data = json.loads(request.body)[0]
        newname = data.get('fields', {}).get('name', None)
        newdescription = data.get('fields', {}).get('description', None)

        clip = Clip()
        clip = clip.get_clip(clip_id)
        form = ClipForm(clip)

        if form.is_valid():
            clip = Clip(name=newname,
                        description=newdescription,
                        pk=clip_id)
            clip.save(update_fields=["name", "description"])
        return HttpResponse(status=201)
