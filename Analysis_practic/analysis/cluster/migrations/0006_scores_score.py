# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0005_remove_scores_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='score',
            field=models.DecimalField(default=2, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
    ]
