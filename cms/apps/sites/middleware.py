from django.core.urlresolvers import reverse
from django.http import Http404

from cms.apps.sites.models import Site


class InteractiveCmsSiteMiddleware(object):
    def process_request(self, request):

        if request.path_info.startswith(reverse('mainadmin:index')):
            print request.user

        if request.path_info.startswith(reverse('useradmin:index')):
            domain = request.META['HTTP_HOST'].split(':')[0]
            try:
                site = Site.objects.get(domain=domain)
                request.site = site
            except Site.DoesNotExist:
                raise Http404('Could not find site matching domain "{}"'.format(domain))
