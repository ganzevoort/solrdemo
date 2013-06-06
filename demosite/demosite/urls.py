from django.conf.urls import patterns, include, url
from demosite.views import CarsSearchView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^cars/', include('cars.urls', namespace='cars')),
    url(r'^search/autocomplete/', 'demosite.views.autocomplete'),
    url(r'^search/', CarsSearchView(), name='haystack_search'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'demosite.views.homepage'),
)
