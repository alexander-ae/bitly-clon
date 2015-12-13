from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

from shortener.models import Link


class ShortURLRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        link = get_object_or_404(Link, slug=kwargs['slug'])
        print 'red: ', link.url
        return link.url
