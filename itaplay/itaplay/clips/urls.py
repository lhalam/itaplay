# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
                       url(r'clips/$', views.ClipView.as_view(), name='clips'),
                       url(r'clips/(?P<pk>\d+)$', views.ClipView.as_view(), name='get_clip'),
                       url(r'delete/(?P<pk>\d+)$', views.ClipView.as_view(), name='clip_delete'),
                       url(r'add_clip/$', views.ClipView.as_view(), name='add_clip'),
                       )
