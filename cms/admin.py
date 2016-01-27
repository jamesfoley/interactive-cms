from django.contrib.admin.sites import AdminSite

class MainAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.is_staff


class UserAdminSite(AdminSite):
    def has_permission(self, request):
        print request.site
        return request.user.is_staff


main_admin_site = MainAdminSite(name='mainadmin')
user_admin_site = UserAdminSite(name='useradmin')
