__author__ = 'camron'
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from models import s

class MediaResource(ModelResource):
    class Meta:
        queryset = Media.objects.all()
        resource_name = 'media'
        filtering = {"title": ALL}
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization



