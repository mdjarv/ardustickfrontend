from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ardustick.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', lambda r : HttpResponseRedirect('frontend/')),
    url(r'^frontend/', include('frontend.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
