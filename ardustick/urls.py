from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
from lightcontrol.models import Device, Remote


class RemoteViewSet(viewsets.ModelViewSet):
    model = Remote

class DeviceViewSet(viewsets.ModelViewSet):
    model = Device


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'remotes', RemoteViewSet)
router.register(r'devices', DeviceViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ardustick.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^$', lambda r : HttpResponseRedirect('frontend/')),
    url(r'^', include(router.urls)),
    url(r'^frontend/', include('frontend.urls')),
    url(r'^lightcontrol/', include('lightcontrol.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
