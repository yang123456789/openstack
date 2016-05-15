from django.conf.urls import patterns, include, url

urlpatterns = patterns('portal.controllers',
    url(r'^/?$', 'customer.index'),
    url(r'^register$', 'customer.register'),
)