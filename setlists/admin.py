from django import forms
from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import Song, Album, Show, Venue, ShowRelation, AlbumRelation 
# Register your models here.

admin.site.register(Song)
#admin.site.register(Album)
admin.site.register(Venue)
#admin.site.register(AlbumRelation)
#admin.site.register(ShowRelation)

class ShowRelationInline(admin.TabularInline):
    model = ShowRelation
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': TextInput(attrs={'size':'40'})},
    }
    ordering = ("track_position",)

class ShowAdmin(admin.ModelAdmin):
    inlines = (ShowRelationInline, )
admin.site.register(Show, ShowAdmin)

class AlbumRelationInline(admin.TabularInline):
    model = AlbumRelation
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': TextInput(attrs={'size':'40'})},
    }
    ordering = ("track_position",)

class AlbumAdmin(admin.ModelAdmin):
    inlines = (AlbumRelationInline, )
    list_display = ('album_title', 'album_date')
admin.site.register(Album, AlbumAdmin)
