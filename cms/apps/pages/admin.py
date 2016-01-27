from django.contrib import admin

from cms.admin import user_admin_site
from cms.apps.pages.models import Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

    def get_queryset(self, request):
        queryset = super(PageAdmin, self).get_queryset(request)
        return queryset.filter(site=request.site)


user_admin_site.register(Page, PageAdmin)
