from django.conf.urls import patterns, include, url

urlpatterns = patterns('portal.controllers',
    # url(r'^$', 'register.index'),
    # url(r'^login$', 'login.validate'),
    url(r'^register$', 'register.register'),
    url(r'^common$', 'common.index'),
    url(r'^system_info$', 'compute.computer.index'),
    # url(r'^ajax$', 'login.ajax_handler')
)