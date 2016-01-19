from django import template

register = template.Library()

@register.filter(name="numberize")
def numberize(note_dict, simple):
    if simple in note_dict:
        return note_dict[simple][0]
