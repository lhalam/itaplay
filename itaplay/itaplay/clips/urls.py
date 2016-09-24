# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',

    url(r'allclips/$', views.ClipView.as_view(), name='clips'),
    url(r'(?P<clip_id>\d+)$', views.ClipView.as_view(), name='get_clip'),
    url(r'delete/(?P<clip_id>\d+)$', views.ClipView.as_view(), name='clip_delete'),
    url(r'update/(?P<clip_id>\d+)$', views.ClipView.as_view(), name='clip_update'),
    url(r'add_clip/$', views.ClipView.as_view(), name='add_clip'),
  
)


