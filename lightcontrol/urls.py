from django.conf.urls import url

urlpatterns = [
    url(r'(?P<device>[0-9]+)/(?P<status>[0-1])/$', 'lightcontrol.views.set_light'),
]