from django.core.urlresolvers import reverse


class InteractiveCmsSiteMiddleware(object):
    def process_response(self, request, response):

        if request.path_info.startswith(reverse('mainadmin:index')):
            print request.user

        return response
