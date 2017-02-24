from django.conf.urls import url
from food import views

urlpatterns = [
    url(r'revenue$', views.revenue),
    url(r'cp$', views.cp),
    url(r'solutionemv', views.report_emv),
    url(r'emv', views.emv),
    url(r'cp_max', views.cp_max),
    url(r'col', views.col),
    url(r'wol', views.wol),
    url(r'solutioneol', views.report_eol),
    url(r'eol', views.eol),
    url(r'$', views.wp),
]
