from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import generic
from .models import *

class ShowIndexView(generic.ListView):
    template_name = 'setlists/index.html'
    context_object_name = 'show_list'
    list_obj = Show.objects.order_by('-show_date')

    def get_queryset(self):
        return self.list_obj

class RecentShowView(ShowIndexView):
    list_obj = Show.objects.order_by('-show_date')[:5]

def song_index(request):
    #songs_all = Song.objects.all()
    songs_all = Song.objects.order_by('song_title') #can probably be handled by the front-end shit later, just being picky for now
    return render(request, 'setlists/song_index.html', {'songs_all': songs_all})

def id_detail(request, show_id):
    mas = get_list_or_404(ShowRelation, show__id=show_id)
    return render(request, 'setlists/show_detail.html', {'mas': mas})

def show_detail(request, d):
    mas = get_list_or_404(ShowRelation.objects.order_by('track_position'), show__show_date=d)
    return render(request, 'setlists/show_detail.html', {'mas': mas})

def song_detail(request, title):
    s = Song.objects.get(simple_title=title)
    if ShowRelation.objects.filter(song=s):
        played_list = get_list_or_404(ShowRelation, song__simple_title=title)
    else:
        played_list = []
    return render(request, 'setlists/song_detail.html', {'s': s, 'played_list': played_list})

def song_not_seen(request, title):
    show_list = Show.objects.all()
    show_list_date = [ i.show_date for i in show_list ]
    show_list_date.sort(reverse=True)

    s = Song.objects.get(simple_title=title)
    if ShowRelation.objects.filter(song=s):
        song_l_version = ShowRelation.objects.filter(song=s).latest('show__show_date')
        song_lv_date = song_l_version.show.show_date
        song_not_seen = show_list_date.index(song_lv_date)
    else:
        song_not_seen = []
        song_l_version = []
    return render(request, 'setlists/song_not_seen.html', {'song_l_version': song_l_version, 'song_not_seen': song_not_seen, 's': s})
