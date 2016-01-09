from django.db import models
from django.utils.text import slugify
import datetime
# Create your models here.

class Song(models.Model):
    song_title = models.CharField(max_length=200)
    simple_title = models.SlugField(default='')
    original_artist = models.CharField(max_length=200, default='Rice Cultivation Society')
    derek_tuning = models.CharField(max_length=20, default='Standard')
    nick_tuning = models.CharField(max_length=20, default='Standard')
    joe_tuning = models.CharField(max_length=20, default='Standard')

    def save(self, *args, **kwargs):
        self.simple_title = slugify(self.song_title)
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.song_title
        
class Album(models.Model):
    album_title = models.CharField(max_length=100)
    album_date = models.IntegerField()
    album_stream = models.URLField(blank=True)

    album_track_01 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_02 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_03 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_04 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_05 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_06 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_07 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_08 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_09 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_10 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_11 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_12 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_13 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_14 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_15 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_16 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_17 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_18 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_19 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    album_track_20 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)

    def __str__(self):
        return self.album_title

    def cleanList(self):
        res = []
        track_list = [self.album_track_01, self.album_track_02, self.album_track_03, self.album_track_04, self.album_track_05,
                self.album_track_06, self.album_track_07, self.album_track_08, self.album_track_09, self.album_track_10,
                self.album_track_11, self.album_track_12, self.album_track_13, self.album_track_14, self.album_track_15,
                self.album_track_16, self.album_track_17, self.album_track_18, self.album_track_19, self.album_track_20]
        res = [ i for i in track_list if i ]
        return res 

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

    show_track_01 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_02 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_03 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_04 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_05 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_06 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_07 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_08 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_09 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_10 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_11 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_12 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_13 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_14 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_15 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_16 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_17 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_18 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_19 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    show_track_20 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="+", null=True, blank=True)

    def __str__(self):
        show_clean_date = self.show_date.strftime('%Y-%m-%d')
        return show_clean_date 

    def cleanList(self):
        res = []
        track_list = [self.show_track_01, self.show_track_02, self.show_track_03, self.show_track_04, self.show_track_05,
                self.show_track_06, self.show_track_07, self.show_track_08, self.show_track_09, self.show_track_10,
                self.show_track_11, self.show_track_12, self.show_track_13, self.show_track_14, self.show_track_15,
                self.show_track_16, self.show_track_17, self.show_track_18, self.show_track_19, self.show_track_20]
        res = [ i for i in track_list if i ]
        return res 
