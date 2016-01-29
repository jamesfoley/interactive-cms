from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


class CmsManageMiddleware(object):
    def process_request(self, request):

        # Check to see if we are inside the management system
        if request.path_info.startswith(reverse('manage:dashboard')):

            # If we are on the login page ignore auth requirement
            if request.path_info.startswith(reverse('manage:login')):
                return None

            # Check to see if we are logged in
            if not request.user or not request.user.is_active or not request.user.is_staff:

                # Take the user to the manage login
                return HttpResponseRedirect('{}?next={}'.format(
                    reverse('manage:login'),
                    request.path_info
                ))

