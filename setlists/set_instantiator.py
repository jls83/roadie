from django.utils.text import slugify
from models import *
import datetime

def DateCreator(src):
    s_date = datetime.datetime.strptime(src, "%Y-%m-%d").date()
    return s_date

def SetSplit(set_src):
    set_clean = set_src.replace(' >', '>,')
    set_split = set_clean.split(', ')
    return set_split

def NoteSplit(note_src):
    note_split = note_src.split(', ')
    return note_split

def SegueSet(src):
    segue = False 
    title = src
    if src[-1] == '>':
        segue = True
        title = src[:-1]
    return title, segue

def NoteSet(src):
    note = ''
    title = src
    if not src[-1].isalpha():
        note = src[-1]
        title = src[:-1]
    return note, title

def SongSplit(song_src):
    song_mid_title, song_segue = SegueSet(song_src)
    song_note, song_title = NoteSet(song_mid_title)
    return song_title, song_segue, song_note

def NoteDictAppendor(src):
    d = {'':''}
    for i in src:
        idx = i.split(' ')[0]
        content = i[2:]
        d[idx] = content
    return d

def SetDictAppendor(set_src, set_date):
    d = {}
    for i in set_src:
        position = set_src.index(i) + 1
        title, segue, index = SongSplit(i)
        d[title] = (set_date, position, segue, note_dict[index])
    return d

############

def venue_get(v, a):
    sv = slugify(v)
    try:
        ven = Venue.objects.get(simple_venue=sv)
    except Venue.DoesNotExist:
        ven = Venue(simple_venue=sv, venue_name=v, venue_address=a)
    finally:
        ven.save()
        return ven

def song_create(s):
    st = slugify(s)
    try:
        son = Song.objects.get(simple_title=st)
    except Song.DoesNotExist:
        son = Song(song_title=s, original_artist="Rice Cultivation Society")
    finally:
        son.save()
        return son

def show_create(d, v, a, n):
    try:
        s = Show.objects.get(show_date=d)
    except Show.DoesNotExist:
        ven = venue_get(v, a)
        s = Show(show_date=d, show_venue=ven, show_notes=n)
    finally:
        s.save()
        return s

def set_create(d, v, a, n):
    for i in d:
        l = d[i]
        son = song_create(i)
        shw = show_create(l[0], v, a, n)
        t_p = l[1]
        t_s = l[2]
        t_n = l[3]
        sr = ShowRelation(song=son, show=shw, track_position=t_p, track_segue=t_s, track_notes=t_n)
        sr.save()

def set_split(d, s, n):
    date_out = DateCreator(date_in)
    set_out = SetSplit(s)
    notes_out = NoteSplit(n)
    note_dict = NoteDictAppendor(notes_out)
    set_dict = SetDictAppendor(set_out, date_out)
    return set_dict

def set_create2(d, v, a, n, s, p):
    d_out = DateCreator(d)
    shw = show_create(d_out, v, a, p)
    s_dict = set_split(d, s, n)
    for i in s_dict:
        l = s_dict[i]
        son = song_create(i)
        shw = show_create(l[0], v, a, n)
        t_p = l[1]
        t_s = l[2]
        t_n = l[3]
        sr = ShowRelation(song=son, show=shw, track_position=t_p, track_segue=t_s, track_notes=t_n)
        sr.save()


date_in = "2014-05-10"
venue_in = "Twisted Shamrock"
addr_in = "Babylon, NY"
set_in = "King Midas, Honey Hide > Bunny In The Sun, MGD, Nothing Was Learned, Broke, Skinned Alive"
notes_in = "Actual setlist may have differed"
#date_in = raw_input("Show Date YYYY-MM-DD: ")
#venue_in = raw_input("Show Venue: ")
#addr_in = raw_input("Show City, ST")
#set_in = raw_input("Set: ")
#notes_in = raw_input("Notes: ")

