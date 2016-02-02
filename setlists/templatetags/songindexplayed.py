from django import template

register = template.Library()

@register.filter(name="playnum")
def played_number(pd, st):
    return pd[st]
