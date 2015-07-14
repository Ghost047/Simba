# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0008_auto_20150307_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wifi_pending',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
