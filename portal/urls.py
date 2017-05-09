from django.conf.urls import patterns, include, url

urlpatterns = patterns('portal.controllers',
    url(r'^/?$', 'login.index'),
    # url(r'^login$', 'login.validate'),
    url(r'^login/validate$', 'login.get_login'),
    url(r'^register$', 'register.register'),
    url(r'^common$', 'common.index'),
    url(r'^system_info$', 'compute.computer.index'),
    url(r'^yang$', 'yang.logs'),
)
