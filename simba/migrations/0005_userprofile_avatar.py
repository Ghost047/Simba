# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0004_auto_20150304_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default=b'/static/images/av_default.jpg', upload_to=b'/static/images/avatars/'),
            preserve_default=True,
        ),
    ]
