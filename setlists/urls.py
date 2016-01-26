from django.conf.urls import url

from . import views

app_name = 'setlists'
urlpatterns = [
    url(r'^$', views.RecentShowView.as_view(), name='index'),
    #Show URLs
    url(r'^shows/$', views.ShowIndexView.as_view(), name='show_index'),
    url(r'^shows/(?P<s_d>(\d{4}-\d{2}-\d{2}))/$', views.ShowDetailView.as_view(), name='show_detail'),
    #Album URLs
    url(r'^albums/$', views.AlbumIndexView.as_view(), name='album_index'),
    url(r'^albums/(?P<album>[\w-]+)/$', views.AlbumDetailView.as_view(), name='album_detail'),
    #Song URLs
    url(r'^songs/$', views.SongIndexView.as_view(), name='song_index'),
    url(r'^songs/(?P<title>[\w-]+)/$', views.SongDetailView.as_view(), name='song_detail'),
    #Venue URLs
    url(r'^venues/$', views.VenueIndexView.as_view(), name='venue_index'),
    url(r'^venues/(?P<venue>[\w-]+)/$', views.VenueDetailView.as_view(), name='venue_detail'),
]
