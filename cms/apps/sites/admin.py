from django.contrib import admin

from cms.admin import main_admin_site
from cms.apps.sites.models import Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'domain']
    list_display_links = list_display


main_admin_site.register(Site, SiteAdmin)
