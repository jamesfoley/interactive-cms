from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User, Group


class MainAdmin(AdminSite):
    pass


main_admin = MainAdmin("Main Admin")
main_admin.register(Group)
main_admin.register(User)
