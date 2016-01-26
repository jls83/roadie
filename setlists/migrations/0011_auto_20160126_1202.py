# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0010_auto_20160117_0238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'ordering': ['-show_date']},
        ),
    ]
