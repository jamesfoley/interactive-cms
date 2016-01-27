from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.shortcuts import render

from cms.admin import user_admin_site
from cms.apps.pages.models import Page


class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'parent')}),
    )
    prepopulated_fields = {'slug': ['title']}

    def changelist_view(self, request, extra_context=None):
        cl = ChangeList(request, self.model, None,
                        None, None, None,
                        None, None, self.list_per_page,
                        self.list_max_show_all, self.list_editable, self)

        context = dict(
            self.admin_site.each_context(request),
            title=cl.title,
            cl=cl,
            has_add_permission=self.has_add_permission(request),
            root_pages=self.get_queryset(request).filter(parent__isnull=True)
        )

        return render(request, 'admin/pages/change_list.html', context=context)

    def get_queryset(self, request):
        queryset = super(PageAdmin, self).get_queryset(request)
        return queryset.filter(site=request.site)

    def save_model(self, request, obj, form, change):
        obj.site = request.site
        obj.save()


user_admin_site.register(Page, PageAdmin)
