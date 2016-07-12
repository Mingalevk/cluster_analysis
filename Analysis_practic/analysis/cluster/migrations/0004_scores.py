# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0003_discipline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('discipline', models.ForeignKey(to='cluster.Discipline')),
                ('student', models.ForeignKey(to='cluster.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
