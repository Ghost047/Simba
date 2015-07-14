# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0009_userprofile_wifi_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='anno',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='matricola',
            field=models.CharField(default=b'0', max_length=128),
            preserve_default=True,
        ),
    ]
