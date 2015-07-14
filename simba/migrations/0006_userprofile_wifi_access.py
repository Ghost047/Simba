# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0005_userprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wifi_access',
            field=models.CharField(default=b'0', max_length=128),
            preserve_default=True,
        ),
    ]
