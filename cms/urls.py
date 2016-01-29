from django.conf.urls import  url, include

from apps.manage import urls as manage_urls

urlpatterns = [
    url(r'^manage/', include(manage_urls, namespace="manage")),
]
