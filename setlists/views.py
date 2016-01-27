from django.views import generic
from .models import *

# Index Views

class MasterIndexView(generic.ListView):
    list_obj = []

    def get_queryset(self):
        return self.list_obj

class ShowIndexView(MasterIndexView):
    template_name = 'setlists/show_index.html'
    context_object_name = 'show_list'
    list_obj = Show.objects.order_by('-show_date')
    date_list = [ i.show_date for i in list_obj ]

class RecentShowView(ShowIndexView): #can probably be replaced with a front-end thing
    template_name = 'setlists/index.html'
    list_obj = Show.objects.order_by('-show_date')[:5]

class AlbumIndexView(MasterIndexView):
    template_name = 'setlists/album_index.html'
    context_object_name = 'album_list'
    list_obj = Album.objects.order_by('-album_date')

class SongIndexView(MasterIndexView):
    template_name = 'setlists/song_index.html'
    context_object_name = 'songs_list'
    list_obj = Song.objects.order_by('song_title')

class VenueIndexView(MasterIndexView):
    template_name = 'setlists/venue_index.html'
    context_object_name = 'venue_list'
    list_obj = Venue.objects.order_by('venue_name')

# Detail Views

class ShowDetailView(generic.DetailView):
    model = Show
    template_name = 'setlists/show_detail.html'
    context_object_name = 'show_obj'
    slug_field = 'show_date'
    slug_url_kwarg = 's_d'

    def show_list_gen(self, show_d):
        return ShowRelation.objects.filter(show__show_date=show_d).order_by('track_position')

    def song_notes_gen(self, s_list):
        d = {}
        count = 1
        for i in s_list:
            if i.track_notes:
                st_nospace = i.song.simple_title.replace('-', '')
                d[st_nospace] = [count, i.track_notes]
                count += 1
        return d

    def prev_next_gen(self, show_d):
        show_current = Show.objects.get(show_date=show_d)
        try:
            show_next = show_current.get_next_by_show_date()
        except Show.DoesNotExist:
            show_next = None
        try:
            show_prev = show_current.get_previous_by_show_date()
        except Show.DoesNotExist:
            show_prev = None
        return [show_prev, show_next]

    def get_context_data(self, **kwargs):
        input_d = self.kwargs['s_d']
        context = super(ShowDetailView, self).get_context_data(**kwargs)
        context['show_tracklist'] = self.show_list_gen(input_d)
        context['show_songnotes'] = self.song_notes_gen( self.show_list_gen(input_d) )
        context['show_prevnext'] = self.prev_next_gen(input_d)
        return context

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'setlists/album_detail.html'
    context_object_name = 'album_obj'
    slug_field = 'simple_title'
    slug_url_kwarg = 'album'

    def album_list_gen(self, album_t):
        return AlbumRelation.objects.filter(album__simple_title=album_t).order_by('track_position')

    def get_context_data(self, **kwargs):
        input_t = self.kwargs['album']
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['album_tracklist'] = self.album_list_gen(input_t)
        return context

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
        p = ShowRelation.objects.filter(song__simple_title=title)
        result = []
        if p:
            result = p
        return result

    def album_list_gen(self, title):
        a = AlbumRelation.objects.filter(song__simple_title=title)
        result = []
        if a:
            result = a
        return result

    def get_context_data(self, **kwargs):
        in_s_t = self.kwargs['title'] # simple_title from URL redirect
        context = super(SongDetailView, self).get_context_data(**kwargs)
        context['played_list'] = self.played_list_gen(in_s_t)
        context['album_list'] = self.album_list_gen(in_s_t)
        context['last_seen_info'] = self.song_not_seen(in_s_t)
        return context

class VenueDetailView(generic.DetailView):
    model = Venue
    template_name = 'setlists/venue_detail.html'
    context_object_name = 'venue_obj'
    slug_field = 'simple_venue'
    slug_url_kwarg = 'venue'

    def venue_shows_gen(self, v_id):
        return Show.objects.filter(show_venue=v_id).order_by('-show_date')

    def get_context_data(self, **kwargs):
        input_v = self.kwargs['venue']
        context = super(VenueDetailView, self).get_context_data(**kwargs)
        venue_id = Venue.objects.get(simple_venue = input_v).id
        context['venue_showlist'] = self.venue_shows_gen(venue_id)
        return context
