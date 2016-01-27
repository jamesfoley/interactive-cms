from django.core.urlresolvers import reverse

from cms.apps.sites.models import Site


class InteractiveCmsSiteMiddleware(object):
    def process_request(self, request):

        if request.path_info.startswith(reverse('mainadmin:index')):
            print request.user

        if request.path_info.startswith(reverse('useradmin:index')):
            domain = request.META['HTTP_HOST'].split(':')[0]
            site = Site.objects.get(domain=domain)
            request.site = site
