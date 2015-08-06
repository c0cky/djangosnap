from django.db import models
import os
from django.core.exceptions import ValidationError
# Create your models here.
from django.contrib.auth.models import User
from tastypie.models import create_api_key
from django.utils.deconstruct import deconstructible

models.signals.post_save.connect(create_api_key, sender=User)

def get_media_path(instance, filename):
    return os.path.join('media', str(instance.id), filename)

# @deconstructible
# class PathAndValidate(object):
#     def __init__(self, sub_path):
#         self.path = sub_path

#     def __call__(self, instance, filename):
#         filesize = instance.file.size
#         megabyte_limit = 5.0
#         if filesize > megabyte_limit*1024*1024:
#             raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
#         ext = os.path.splitext(instance.name)[1]
#         valid_extensions = ['.mp4','.png','.jpg']
#         if not ext in valid_extensions:
#             raise ValidationError(u'File not supported!')
#         # ext = filename.split('.')[-1]
#         # # set filename as random string
#         # filename = '{}.{}'.format(uuid4().hex, ext)
#         # return the whole path to the file
#         return os.path.join(self.path, filename)

# path_and_validate = PathAndValidate("/djangosnap/%Y/%m/%d/")


class Media(models.Model):
    mediafile = models.FileField(upload_to='djangosnap/%Y/%m/%d')
    approved = models.BooleanField(default=False)
    up_vote = models.IntegerField(blank=True, default=0, null=True)
    down_vote = models.IntegerField(blank=True, default=0, null=True)
    long_position   = models.DecimalField (max_digits=8, decimal_places=3, blank=True, default=0, null=True)
    lat_position   = models.DecimalField (max_digits=8, decimal_places=3, blank=True, default=0, null=True)
    upload_time = models.TimeField((u"Upload Date"), auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.mediafile.name
