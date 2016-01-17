# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0009_album_simple_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['simple_title']},
        ),
    ]
