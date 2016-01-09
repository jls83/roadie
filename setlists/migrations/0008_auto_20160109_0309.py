# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0007_auto_20160109_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='showrelation',
            name='track_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='showrelation',
            name='track_segue',
            field=models.BooleanField(default=False),
        ),
    ]
