from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import *

def index(request):
    latest_show_list = Show.objects.order_by('-show_date')[:5]
    return render(request, 'setlists/index.html', {'latest_show_list': latest_show_list})

def show_index(request):
    show_all = Show.objects.order_by('-show_date')
    #show_all = Show.objects.all() #can probably sort with a front-end implementation of some shit
    return render(request, 'setlists/show_index.html', {'show_all': show_all})

def song_index(request):
    #songs_all = Song.objects.all()
    songs_all = Song.objects.order_by('song_title') #can probably be handled by the front-end shit later, just being picky for now
    return render(request, 'setlists/song_index.html', {'songs_all': songs_all})

def id_detail(request, show_id):
    mas = get_list_or_404(ShowRelation, show__id=show_id)
    return render(request, 'setlists/show_detail.html', {'mas': mas})

def show_detail(request, d):
    mas = get_list_or_404(ShowRelation, show__show_date=d)
    return render(request, 'setlists/show_detail.html', {'mas': mas})

def song_detail(request, title):
    s = Song.objects.get(simple_title=title)
    if ShowRelation.objects.filter(song=s):
        played_list = get_list_or_404(ShowRelation, song__simple_title=title)
    else:
        played_list = []
    return render(request, 'setlists/song_detail.html', {'s': s, 'played_list': played_list})

#def song_detail(request, title):
#    played_list = get_list_or_404(ShowRelation, song__simple_title=title)
#    return render(request, 'setlists/song_detail.html', {'played_list': played_list})
