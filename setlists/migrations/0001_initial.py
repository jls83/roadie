# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_title', models.CharField(max_length=100)),
                ('album_date', models.IntegerField()),
                ('album_stream', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show_date', models.DateField()),
                ('show_stream', models.URLField()),
                ('show_notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_title', models.CharField(max_length=200)),
                ('original_artist', models.CharField(default=b'Rice Cultivation Society', max_length=200)),
                ('derek_tuning', models.CharField(default=b'Standard', max_length=20)),
                ('nick_tuning', models.CharField(default=b'Standard', max_length=20)),
                ('joe_tuning', models.CharField(default=b'Standard', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('venue_name', models.CharField(max_length=200)),
                ('venue_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='show_venue',
            field=models.ForeignKey(to='setlists.Venue'),
        ),
    ]
