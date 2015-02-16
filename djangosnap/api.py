__author__ = 'camron'
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authentication import BasicAuthentication
from models import Media

class MediaResource(ModelResource):
    class Meta:
        queryset = Media.objects.all()
        resource_name = 'media'
        filtering = {"title": ALL}
        authentication = BasicAuthentication()

