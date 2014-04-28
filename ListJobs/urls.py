from django.conf.urls import patterns, include, url
from .views import ListJobsView
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aj_final.views.home', name='home'),
    # url(r'^aj_final/', include('aj_final.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^ListJobs$', ListJobsView.as_view(), name='jobs'),
)
