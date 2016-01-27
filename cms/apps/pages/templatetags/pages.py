from django.template import Library

from cms.apps.pages.models import Page

register = Library()

@register.assignment_tag()
def get_child_pages(page):
    return Page.objects.filter(site=page.site, parent=page)
