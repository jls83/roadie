from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import generic
from .models import *

class ShowIndexView(generic.ListView):
    template_name = 'setlists/show_index.html'
    context_object_name = 'show_list'
    list_obj = Show.objects.order_by('-show_date')
    date_list = [ i.show_date for i in list_obj ]

    def get_queryset(self):
        return self.list_obj

class RecentShowView(ShowIndexView): #can probably be replaced with a front-end thing
    template_name = 'setlists/index.html'
    list_obj = Show.objects.order_by('-show_date')[:5]

class ShowDetailView(generic.ListView):
    model = Show
    template_name = 'setlists/show_detail.html'
    context_object_name = 'show_obj'
    slug_field = 'show_date'
    slug_url_kwarg = 's_d'

    def show_list_gen(self, show_d):
        return ShowRelation.objects.filter(show__show_date=show_d).order_by('track_position')

    def get_context_data(self, **kwargs):
        input_d = self.kwargs['s_d']
        context = super(ShowDetailView, self).get_context_data(**kwargs)
        context['mas'] = self.show_list_gen(input_d)
        return context

class SongIndexView(generic.ListView):
    template_name = 'setlists/song_index.html'
    context_object_name = 'songs_list'
    songs_list = Song.objects.order_by('song_title')

    def get_queryset(self):
        return self.songs_list

class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'setlists/song_detail.html'
    context_object_name = 'song_info'
    slug_field = 'simple_title'
    slug_url_kwarg = 'title'

    def song_not_seen(self, title):
        s_l = ShowIndexView.date_list
        l_version = []
        last_seen = []
        s = ShowRelation.objects.filter(song__simple_title=title)
        if s:
            l_version = s.latest('show__show_date')
            lv_date = l_version.show.show_date
            last_seen = s_l.index(lv_date)
        return (l_version, last_seen)

    def played_list_gen(self, title):
        return get_list_or_404(ShowRelation.objects.order_by('-show__show_date'), song__simple_title=title)

    def get_context_data(self, **kwargs):
        in_s_t = self.kwargs['title'] # simple_title from URL redirect
        context = super(SongDetailView, self).get_context_data(**kwargs)
        context['played_list'] = self.played_list_gen(in_s_t)
        context['last_seen_info'] = self.song_not_seen(in_s_t)
        return context
