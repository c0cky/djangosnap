__author__ = 'camron'
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from models import Media
from django.contrib.auth.models import User

class MediaResource(ModelResource):
    class Meta:
        queryset = Media.objects.all()
        resource_name = 'media'
        filtering = {"title": ALL}
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class UserResource(ModelResource):
    class Meta:
        allowed_methods = ['post']
        object_class = User()
        include_resource_uri = False
        fields = ['username']

    def obj_create(self, bundle, request=None, **kwargs):
        username, password = bundle.data['username'], bundle.data['password']
        try:
            bundle.obj = User.objects.create_user(username, '', password)
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle


