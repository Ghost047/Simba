# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simba', '0014_userprofile_is_fc'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetaCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=128)),
                ('gen_date', models.DateField(auto_now_add=True)),
                ('valid', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=0),
            preserve_default=True,
        ),
    ]
