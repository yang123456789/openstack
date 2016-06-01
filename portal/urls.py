from django.conf.urls import patterns, include, url

urlpatterns = patterns('portal.controllers',
    url(r'^/?$', 'resigter.index'),
    url(r'^login$', 'login.validate'),
    url(r'^register$', 'resigter.resigter'),
    url(r'^common$', 'common.index'),
)