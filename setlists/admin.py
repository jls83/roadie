from django.contrib import admin
from .models import Song, Album, Show, Venue
# Register your models here.

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Show)
admin.site.register(Venue)