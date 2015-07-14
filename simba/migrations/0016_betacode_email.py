# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0015_auto_20150329_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='betacode',
            name='email',
            field=models.CharField(default=b'0', max_length=128),
            preserve_default=True,
        ),
    ]
