""" URLs used by the jobs app """
from django.conf.urls import url

from views import auth, dashboard

urlpatterns = [
    url(r"^login/$", auth.Login.as_view(), name='login'),
    url(r"^logout/$", auth.Logout.as_view(), name='logout'),

    url(r"^$", dashboard.Dashboard.as_view(), name='dashboard'),
]
