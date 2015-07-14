# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0016_betacode_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=128)),
                ('date', models.DateField(auto_now_add=True)),
                ('member', models.OneToOneField(to='simba.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
