# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0008_auto_20160109_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='simple_title',
            field=models.SlugField(default=b'', editable=False),
        ),
    ]
