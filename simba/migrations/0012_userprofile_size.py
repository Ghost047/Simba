# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0011_auto_20150314_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='size',
            field=models.CharField(default=b'M', max_length=128),
            preserve_default=True,
        ),
    ]
