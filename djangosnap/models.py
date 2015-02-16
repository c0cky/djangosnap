from django.db import models
import os
from django.core.exceptions import ValidationError
# Create your models here.
def get_media_path(instance, filename):
    return os.path.join('media', str(instance.id), filename)

class Media(models.Model):
    def validate_media(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
        ext = os.path.splitext(fieldfile_obj.name)[1]
        valid_extensions = ['.mp4','.png','.jpg']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported!')

    mediafile = models.FileField(upload_to='djangosnap/%Y/%m/%d', validators=[validate_media])
    approved = models.BooleanField(default=False)
    long_position   = models.DecimalField (max_digits=8, decimal_places=3, blank=True, default=0, null=True)
    lat_position   = models.DecimalField (max_digits=8, decimal_places=3, blank=True, default=0, null=True)
    upload_time = models.TimeField((u"Upload Date"), auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.mediafile.name
