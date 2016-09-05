from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.MonitorView.as_view(), name='monitor'),

]