from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'manage/dashboard/dashboard.html'


