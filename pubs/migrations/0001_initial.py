# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search_string',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('searchstring', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('trigger_counter', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
