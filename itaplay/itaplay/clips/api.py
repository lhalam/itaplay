from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from .models import Clip


class ClipResource(ModelResource):
    """
    API Facet
    """
    class Meta:
        queryset = Clip.objects.all()
        resource_name = 'clip'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True