from django import forms
from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import Song, Album, Show, Venue, ShowRelation, AlbumRelation 
# Register your models here.

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Venue)
admin.site.register(AlbumRelation)
#admin.site.register(ShowRelation)

class ShowRelationInline(admin.TabularInline):
    model = ShowRelation
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': TextInput(attrs={'size':'40'})},
    }

#class ShowRelationAdmin(admin.ModelAdmin):
#    list_display = ('get_show_date', 'track_position', 'get_song_title',)
#    def get_show_date(self, obj):
#        return obj.show.show_date
#    def get_song_title(self, obj):
#        return obj.song.song_title
#    get_show_date.admin_order_field = 'show__show_date'
#    get_song_title.admin_order_field = 'song__song_title'
#    #pass

class ShowAdmin(admin.ModelAdmin):
    inlines = (ShowRelationInline, )
admin.site.register(Show, ShowAdmin)
