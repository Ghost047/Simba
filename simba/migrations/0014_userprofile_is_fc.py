# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0013_auto_20150320_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_fc',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
