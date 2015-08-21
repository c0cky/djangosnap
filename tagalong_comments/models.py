from django.db import models
from django_comments.models import Comment

class TagalongComment(Comment):
    class Meta:
        app_label = 'tagalong_comments'

    up_vote = models.IntegerField(blank=True, default=0, null=True)
    down_vote = models.IntegerField(blank=True, default=0, null=True)