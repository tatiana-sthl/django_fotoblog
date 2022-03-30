from time import timezone
from django import template

register = template.Library()

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

@register.filter
def model_type(value):
    return type(value).__name__

@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'vous'
    return user.username


