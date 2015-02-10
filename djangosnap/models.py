from django.db import models
import os
# Create your models here.
def get_media_path(instance, filename):
    return os.path.join('media', str(instance.id), filename)

class Media(models.Model):
    mediafile = models.FileField(upload_to='djangosnap/%Y/%m/%d') #

