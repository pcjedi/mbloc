from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mbloc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^pubs/', include('pubs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
