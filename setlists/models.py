from django.db import models
from django.utils.text import slugify
import datetime
# Create your models here.

class Song(models.Model):
    song_title = models.CharField(max_length=200)
    simple_title = models.SlugField(default='', editable=False)
    original_artist = models.CharField(max_length=200, default='Rice Cultivation Society')
    derek_tuning = models.CharField(max_length=20, default='Standard')
    nick_tuning = models.CharField(max_length=20, default='Standard')
    joe_tuning = models.CharField(max_length=20, default='Standard')

    class Meta:
        ordering = ['simple_title']

    def save(self, *args, **kwargs):
        self.simple_title = slugify(self.song_title)
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.song_title
        
class Album(models.Model):
    album_title = models.CharField(max_length=100)
    simple_title = models.SlugField(default='', editable=False)
    album_date = models.IntegerField()
    album_stream = models.URLField(blank=True)
    album_tracks = models.ManyToManyField(Song, through='AlbumRelation')

    def save(self, *args, **kwargs):
        self.simple_title = slugify(self.album_title)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.album_title

class Venue(models.Model):
    venue_name = models.CharField(max_length=200)
    venue_address = models.CharField(max_length=200)

    def __str__(self):
        return self.venue_name
    
class Show(models.Model):
    show_date = models.DateField()
    show_venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    show_stream = models.URLField(blank=True)
    show_notes = models.TextField(blank=True)
    show_tracks = models.ManyToManyField(Song, through='ShowRelation')

    def __str__(self):
        show_clean_date = self.show_date.strftime('%Y-%m-%d')
        return show_clean_date 

class AlbumRelation(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_position = models.IntegerField()

    def __str__(self):
        relation_title ='{0} - {1}. {2}'.format(self.album.album_title, self.track_position, self.song.song_title)
        return relation_title

class ShowRelation(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    track_position = models.IntegerField()
    track_segue = models.BooleanField(default=False)
    track_notes = models.TextField(blank=True)

    def __str__(self):
        relation_title ='{0} - {1}. {2}'.format(self.show.show_date, self.track_position, self.song.song_title)
        return relation_title
