from django.db import models
import os
# Create your models here.
def get_media_path(instance, filename):
    return os.path.join('media', str(instance.id), filename)

class Media(models.Model):
    mediafile = models.FileField(upload_to='djangosnap/%Y/%m/%d')
    approved = models.BooleanField(default=False)
    long_position   = models.DecimalField (max_digits=8, decimal_places=3, blank=True, default=0, null=True)
    lat_position   = models.DecimalField (max_digits=8, decimal_places=3, blank=True, default=0, null=True)
    upload_time = models.TimeField((u"Upload Date"), auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.mediafile
