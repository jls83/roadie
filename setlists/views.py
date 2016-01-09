from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Show, Album, Song, Venue
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


def date_detail(request, date):
    try:
        show = Show.objects.get(show_date=date)
        show_track_list = show.cleanList()
    except Show.DoesNotExist:
        raise Http404("Show does not exist!")
    return render(request, 'setlists/show_detail.html', {'show': show, 'show_track_list': show_track_list})

def song_detail(request, title):
    try:
        song = Song.objects.get(simple_title=title)
    except Song.DoesNotExist:
        raise Http404("Show does not exist!")
    return render(request, 'setlists/song_detail.html', {'song': song})
