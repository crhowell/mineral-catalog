from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def is_active(request, name, *args):
    if name:
        path = reverse(name, args=args)
        if request.path == path:
            return ' active '
    return ''
