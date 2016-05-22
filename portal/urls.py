from django.conf.urls import patterns, include, url

urlpatterns = patterns('portal.controllers',
    url(r'^/?$', 'resigter.index'),
    url(r'^register$', 'resigter.resigter'),
)