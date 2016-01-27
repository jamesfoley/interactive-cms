from django.contrib import admin
from cms.admin.main import main_admin
from cms.apps.sites.models import Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'domain']
    list_display_links = list_display


main_admin.register(Site, SiteAdmin)
