from django.contrib import admin

from cms.admin import user_admin_site
from cms.apps.pages.models import Page


class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'parent')}),
    )

    prepopulated_fields = {'slug': ['title']}

    def get_queryset(self, request):
        queryset = super(PageAdmin, self).get_queryset(request)
        return queryset.filter(site=request.site)

    def save_model(self, request, obj, form, change):
        obj.site = request.site
        obj.save()


user_admin_site.register(Page, PageAdmin)
