from setlists.models import *
import datetime

def set_create(d, v):
    try:
        s = Show.objects.get(show_date=d)
    except Show.DoesNotExist:
        s = Show(show_date=d, show_venue=v)
    s.save()

def venue_get(sv):
    return Venue.objects.get(simple_venue=sv)

venue_in = raw_input("Venue: ")

venue_got = venue_get(venue_in)

print venue_got.venue_name
