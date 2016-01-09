from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Show, Album, Song, Venue, ShowRelation, AlbumRelation
# Create your views here.

def index(request):
    latest_show_list = Show.objects.order_by('-show_date')[:5]
    return render(request, 'setlists/index.html', {'latest_show_list': latest_show_list})

def detail(request, show_id):
    try:
        show = Show.objects.get(pk=show_id)
        show_track_list = show.cleanList()
    except Show.DoesNotExist:
        raise Http404("Show does not exist!")
    return render(request, 'setlists/show_detail.html', {'show': show, 'show_track_list': show_track_list})

def date_detail(request, d):
    try:
        s = Show.objects.get(show_date=d)
        s_list = s.show_tracks.all()
        mas = [ShowRelation.objects.get(show=s, song=i) for i in s_list]
    except Show.DoesNotExist:
        raise Http404("Show does not exist!")
    return render(request, 'setlists/show_detail.html', {'s': s, 'mas': mas})

def song_detail(request, title):
    try:
        song = Song.objects.get(simple_title=title)
    except Song.DoesNotExist:
        raise Http404("Show does not exist!")
    return render(request, 'setlists/song_detail.html', {'song': song})
