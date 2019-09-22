from django.conf.urls import url

from holydays.views import *

urlpatterns = [
    url(r'^admin/updateholydays/$', HolydaysAdmin.as_view()),
    url(r'^getcountrys/$', CountrysListView.as_view()),
    url(r'^getholydays/$', Holyday.as_view()),
]