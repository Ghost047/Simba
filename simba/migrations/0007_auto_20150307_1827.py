# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simba', '0006_userprofile_wifi_access'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField(auto_now_add=True)),
                ('desc', models.CharField(max_length=500)),
                ('maino', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('deadline', models.DateField(auto_now_add=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('desc', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='simba.Evento')),
                ('sender', models.OneToOneField(related_name='task_sender', to=settings.AUTH_USER_MODEL)),
                ('target', models.OneToOneField(related_name='task_target', default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
