# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0004_auto_20160107_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='simple_title',
            field=models.SlugField(default=b''),
        ),
    ]
