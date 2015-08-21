# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_update_user_email_field_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagalongComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='django_comments.Comment')),
                ('up_vote', models.IntegerField(default=0, null=True, blank=True)),
                ('down_vote', models.IntegerField(default=0, null=True, blank=True)),
            ],
            bases=('django_comments.comment',),
        ),
    ]
