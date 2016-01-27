from django.contrib.admin.sites import AdminSite


class UserAdmin(AdminSite):
    pass


user_admin = UserAdmin(name="User Admin")
