from django.conf.urls import url

from . import views

app_name = 'setlists'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shows/$', views.show_index, name='show_index'),
    url(r'^show_id/(?P<show_id>[0-9]+)/$', views.id_detail, name='id_detail'),
    url(r'^shows/(?P<d>\d{4}-\d{2}-\d{2})/$', views.show_detail, name='show_detail'),
    url(r'^songs/$', views.song_index, name='song_index'),
    url(r'^songs/(?P<title>[\w-]+)/$', views.song_detail, name='song_detail'),
    url(r'^notseen/(?P<title>[\w-]+)/$', views.song_not_seen, name='song_not_seen'),
]
