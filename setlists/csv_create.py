# This script will take in a set, and associated per-song notes, and put out a dict in this format:
# song_dict[title] = (show date, track position, segue, per-track note)
# Title and note are both strings, position is an integer, show date is a datetime object, and segue is a boolean

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

date_in = "2014-05-16"
venue_in = "Soul Sounds Records"
addr_in = "Sayville, NY"
set_in = "Honey Hide > MGD, Bunny In The Sun, King Midas, Nothing Was Learned, Broke, Seaturtles, Skinned Alive"
notes_in = ""
#date_in = raw_input("Show Date YYYY-MM-DD: ")
#set_in = raw_input("Set: ")
#notes_in = raw_input("Notes: ")

date_out = DateCreator(date_in)
set_out = SetSplit(set_in)
notes_out = NoteSplit(notes_in)
note_dict = NoteDictAppendor(notes_out)
set_dict = SetDictAppendor(set_out, date_out)

#for i in set_dict:
    #print i
