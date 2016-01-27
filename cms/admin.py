from django.contrib.admin.sites import AdminSite
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from cms.apps.users.models import User


class MainAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.is_staff


class UserAdminSite(AdminSite):
    def has_permission(self, request):
        print request.site
        return request.user.is_staff


main_admin_site = MainAdminSite(name='mainadmin')
user_admin_site = UserAdminSite(name='useradmin')


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal information', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        ('Personal information', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_active')

    filter_horizontal = ()

    ordering = ()


main_admin_site.register(User, UserAdmin)
