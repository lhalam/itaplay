from django.core import serializers
from django.http import HttpResponse
from forms import ClipForm
from models import Clip
from django.views.generic import View
import json
from utils.amazons3service import save_on_amazon_with_boto, delete_from_amazon_with_boto

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
                           )

            clipfile = request.FILES['file']

            newclip.url = save_on_amazon_with_boto(clipfile)
            newclip.mimetype = newclip.generate_mimetype(newclip.url)

            newclip.save()

            return HttpResponse(status=201)

    """
    Handling DELETE method.
    
    :return: HttpResponse with code 201 if clip is deleted.
    """

    def delete(self, request, clip_id):
        data = json.loads(request.body)
        clip = Clip.get_clip(clip_id=data['pk'])
        data = serializers.serialize('json', clip).encode('utf-8')
        # convert to dict
        data = json.loads(data)[0]
        # get current clip url
        url = data.get('fields', {}).get('url', None)
        # delete file on amazon
        delete_from_amazon_with_boto(url)
        clip.delete()
        return HttpResponse(status=201)

    """
    Handling GET method for all clips.
    
    :return: all clips
    """

    def get(self, request, clip_id=None):
        if not clip_id:
            clips = Clip.get_all_clips()
            data = serializers.serialize('json', clips)
            return HttpResponse(data, content_type='application/json')

        clip = Clip.get_clip(clip_id)
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
