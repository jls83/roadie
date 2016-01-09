# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0003_auto_20160102_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_stream',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_stream',
            field=models.URLField(blank=True),
        ),
    ]
