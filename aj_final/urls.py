from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aj_final.views.home', name='home'),
    # url(r'^aj_final/', include('aj_final.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ListJobs.urls', namespace='listjobs')),
)
