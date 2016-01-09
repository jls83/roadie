from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shows/$', views.show_index, name='show_index'),
    url(r'^show_id/(?P<show_id>[0-9]+)/$', views.id_detail, name='id_detail'),
    url(r'^shows/(?P<d>\d{4}-\d{2}-\d{2})/$', views.date_detail, name='date_detail'),
    url(r'^songs/$', views.song_index, name='song_index'),
    url(r'^songs/(?P<title>[\w-]+)/$', views.song_detail, name='song_detail'),
]
