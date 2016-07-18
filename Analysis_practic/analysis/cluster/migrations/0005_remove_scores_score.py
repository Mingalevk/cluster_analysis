# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0004_scores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scores',
            name='score',
        ),
    ]
