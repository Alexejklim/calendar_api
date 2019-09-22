from django.conf.urls import url

from mainapp.views import Events, EventsDay, EventsMonth

urlpatterns = [
    url(r'^event/$', Events.as_view()),
    url(r'^event/day/$', EventsDay.as_view()),
    url(r'^event/month/$', EventsMonth.as_view()),
]
