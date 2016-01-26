# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0011_auto_20160126_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='simple_venue',
            field=models.SlugField(default=b'', editable=False),
        ),
    ]
