from django.conf.urls import include, url
from admin.main import main_admin
from admin.user import user_admin

urlpatterns = [
    url(r'^main-admin/', include(main_admin.urls)),
    url(r'^user-admin/', include(user_admin.urls)),
]
