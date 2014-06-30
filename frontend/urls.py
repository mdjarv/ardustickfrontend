from django.conf.urls import url
from frontend.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
]