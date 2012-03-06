from coffin.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tickets.views.whiteboard', name='whiteboard'),
    url(r'^min$', 'tickets.views.whiteboard_min', name='whiteboard_min'),
    url(r'^refresh$', 'tickets.views.refresh', name='refresh'),
    url(r'^modal/(?P<ticket_no>\d+)$', 'tickets.views.modal', name='modal'),
    url(r'^status_update/(?P<ticket_no>\d+)/(?P<status_id>\d+)$', 'tickets.views.status_update', name='status_update')
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
