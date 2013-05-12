from django.conf.urls import patterns, url

from .views import ListView, DetailView


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(), name='detail'),
)
