from django.template import  Library
from classytags.core import Tag, Options
from django.utils.safestring import SafeUnicode
from django.core.urlresolvers import reverse

from classytags.arguments import Argument, MultiValueArgument

register = Library()


class UrlReverse(Tag):
    name = 'url_reverse'
    options = Options(
        Argument('name', required=True, resolve=False),
        MultiValueArgument('values', required=False, resolve=True),
    )

    def render_tag(self, context, name=None, values=None, varname=None):
        if len(values) is 1:
            if not type(values[0]) in [int, str, unicode, SafeUnicode]:
                values = values[0]
        return '%s' % reverse(name, args=values).lower()[1:]


register.tag(UrlReverse)