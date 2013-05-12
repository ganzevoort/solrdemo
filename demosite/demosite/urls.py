from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^cars/', include('cars.urls', namespace='cars')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'demosite.views.homepage'),
)
