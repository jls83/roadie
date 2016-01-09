# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0006_auto_20160109_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='simple_title',
            field=models.SlugField(default=b'', editable=False),
        ),
    ]
