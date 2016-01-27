from django.conf.urls import include, url
from cms.admin import main_admin_site, user_admin_site

urlpatterns = [
    url(r'^cms-admin/', main_admin_site.urls),
    url(r'^admin/', user_admin_site.urls),
]
