# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_track_01',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_02',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_03',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_04',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_05',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_06',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_07',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_08',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_09',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_10',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_11',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_12',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_13',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_14',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_15',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_16',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_17',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_18',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_19',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_track_20',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_01',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_02',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_03',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_04',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_05',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_06',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_07',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_08',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_09',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_10',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_11',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_12',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_13',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_14',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_15',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_16',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_17',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_18',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_19',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='show_track_20',
            field=models.ForeignKey(related_name='+', to='setlists.Song', null=True),
        ),
    ]
