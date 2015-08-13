__author__ = 'camron'
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from models import Media
from django.contrib.auth.models import User
from tagalong_comments.models import TagalongComment
from django.forms.models import model_to_dict


class MediaResource(ModelResource):
    comments = fields.ToManyField('djangosnap.api.resources.TagalongCommentResource', 'tagalong_comments')

    class Meta:
        queryset = Media.objects.all()
        resource_name = 'media'
        filtering = {"title": ALL}
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

    def dehydrate(self, bundle):
    	comments = TagalongComment.objects.filter(object_pk=bundle.data['id'])
        bundle.data['comments'] = [model_to_dict(c) for c in comments]
        return bundle

    # def hydrate(self, bundle):
    #     if 'comments' in bundle.data:
    #         bundle.obj.comments = VocabularyResource().get_via_uri(
    #             bundle.data['vocabulary'])

    #     bundle.obj.display_name = bundle.data['display_name']
    #     return bundle

class TagalongCommentResource(ModelResource):
	class Meta:
		queryset = TagalongComment.objects.all()
# class CommentResource(ModelResource):
#     media = fields.ForeignKey(MediaResource, 'media')
#     class Meta:
#         queryset = Comment.objects.all()
#         filtering = {
#             'media': ALL_WITH_RELATIONS,
#         }

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


