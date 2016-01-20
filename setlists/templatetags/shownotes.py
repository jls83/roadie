from django import template

register = template.Library()

@register.filter(name="numberize")
def numberize(note_dict, simple):
    if simple in note_dict:
        return note_dict[simple][0]

@register.filter(name="listify")
def listify(note_dict):
    note_idx = sorted(note_dict, key=note_dict.get)
    note_list = [ note_dict[i] for i in note_idx ]
    return note_list
