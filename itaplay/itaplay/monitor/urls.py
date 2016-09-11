from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.GetMonitorView.as_view(), name='monitor'),
    url(r'^get_by_mac/(?P<mac>(\w\:?)+)/$', views.MonitorView.as_view()),
]