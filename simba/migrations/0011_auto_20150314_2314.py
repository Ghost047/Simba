# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0010_auto_20150314_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='indirizzo',
            field=models.CharField(default=b'scienze delle merendine', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='anno',
            field=models.CharField(default=b'primo', max_length=128),
            preserve_default=True,
        ),
    ]
