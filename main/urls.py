from django.conf.urls import url
from main import views
urlpatterns = [
    url(r'wp', views.wp),
    url(r'solutionemv', views.report_emv),
    url(r'emv', views.emv),
    url(r'cp_max', views.cp_max),
    url(r'col', views.col),
    url(r'wol', views.wol),
    url(r'solutioneol', views.report_eol),
    url(r'eol', views.eol),
    url(r'$', views.index),
]
